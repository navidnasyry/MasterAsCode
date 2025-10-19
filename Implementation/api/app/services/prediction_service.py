import numpy as np

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
