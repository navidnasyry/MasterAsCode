import numpy as np
from tensorflow.keras.models import Model


def prepare_engine_sequence(engine_df, sequence_length, sequence_cols):
    """Prepares padded or truncated sequence for model input."""
    engine_sequence = engine_df[sequence_cols].values
    num_elements = engine_sequence.shape[0]

    if num_elements < sequence_length:
        padding = np.zeros((sequence_length - num_elements, engine_sequence.shape[1]))
        engine_sequence = np.concatenate((padding, engine_sequence), axis=0)
    elif num_elements > sequence_length:
        engine_sequence = engine_sequence[-sequence_length:]

    return np.asarray([engine_sequence]).astype(np.float32)


def predict_rul(model, engine_sequence):
    """Predict RUL using loaded LSTM model."""
    predicted_rul = model.predict(engine_sequence)
    return float(predicted_rul[0][0])


# برای inference و attribution (در میکروسرویس)
def get_rul_and_attribution(model, input_data, sensor_names):  # input_data: (1, sequence_length, nb_features)
    # Get the attention layer from the trained model by its name
    attention_layer_instance = model.get_layer('attention_layer_output')

    # Create a new model that outputs:
    # 1. The RUL prediction (model.output)
    # 2. The 'context' vector from the attention layer (attention_layer_instance.output[0])
    # 3. The 'alpha' (temporal attention weights) from the attention layer (attention_layer_instance.output[1])
    intermediate_model = Model(inputs=model.input,
                               outputs=[model.output,
                                        attention_layer_instance.output[0], # Context vector
                                        attention_layer_instance.output[1]]) # Alpha (temporal attention)

    rul, context_vector, alpha_temporal = intermediate_model.predict(input_data)

    # Calculate sensor impacts from the context vector
    # context_vector has shape (batch_size, nb_features)
    # For a single input sample, context_vector[0] gives the feature-wise contributions.
    sensor_impacts_raw = {}
    if context_vector.shape[0] == 1:
        feature_contributions_abs = np.abs(context_vector[0])
        total_abs_contribution = np.sum(feature_contributions_abs)

        if total_abs_contribution > 0:
            normalized_impacts = (feature_contributions_abs / total_abs_contribution).flatten()
        else:
            normalized_impacts = np.zeros_like(feature_contributions_abs).flatten()
        
        for i, sensor_name in enumerate(sensor_names):
            sensor_impacts_raw[sensor_name] = normalized_impacts[i]
    else:
        # Fallback for batch inputs if needed, though for attribution, single sample is common
        print("Warning: Context vector not for single sample, using equal distribution for sensor impacts.")
        for sensor_name in sensor_names:
            sensor_impacts_raw[sensor_name] = 1.0 / len(sensor_names)

    # Exclude 'unit_number' and 'time_in_cycles' and 'cycle_norm'
    excluded_sensors = ['unit_number', 'time_in_cycles', 'cycle_norm']
    filtered_impacts = {s: imp for s, imp in sensor_impacts_raw.items() if s not in excluded_sensors}

    # Re-normalize the filtered impacts so they sum to 1
    sum_after_filter = sum(filtered_impacts.values())
    if sum_after_filter > 0:
        re_normalized_impacts = {s: imp / sum_after_filter for s, imp in filtered_impacts.items()}
    else:
        re_normalized_impacts = {s: 0.0 for s in filtered_impacts.keys()} # All impacts are 0 if sum is 0

    # Sort the filtered and re-normalized impacts by value in descending order
    sorted_impacts = dict(sorted(re_normalized_impacts.items(), key=lambda item: item[1], reverse=True))

    return {"rul": rul[0][0], "sensor_impacts": sorted_impacts}
