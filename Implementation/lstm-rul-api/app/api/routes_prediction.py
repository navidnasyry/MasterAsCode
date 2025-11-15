from fastapi import APIRouter
from app.models.lstm_model import load_lstm_model
from app.services.prediction_service import prepare_engine_sequence, predict_rul, get_rul_and_attribution
from app.schemas.prediction_schemas import EngineData, PredictionResponse, EngineRULResponse
from app.core.config import MODEL_BASE_PATH

import numpy as np

router = APIRouter()

# Load model once at startup
try:
    model, history, model_data = load_lstm_model(MODEL_BASE_PATH)
    lstm_test_df = model_data["lstm_test_df"]
    sequence_length = model_data["sequence_length"]
    sequence_cols = model_data["sequence_cols"]
except Exception as e:
    model = None
    lstm_test_df = None
    sequence_length = None
    sequence_cols = None
    print(f"❌ Error loading LSTM model: {e}")


@router.get("/predict_rul/{engine_number}", response_model=EngineRULResponse)
def predict_rul_for_engine_api(engine_number: int, k_most_effictive: int = 5):
    """Predict RUL for an engine in test dataset.
    
        Example curl reqeust: 
            curl `http://localhost:8000/api/predict/predict_rul/10`
    """
    if model is None:
        return {"error": "Model not loaded."}

    engine_df = lstm_test_df[lstm_test_df["unit_number"] == engine_number]
    if engine_df.empty:
        return {"error": f"Engine number {engine_number} not found."}

    seq_array_engine = prepare_engine_sequence(engine_df, sequence_length, sequence_cols)
    attribution_results = get_rul_and_attribution(model, seq_array_engine, sequence_cols)
    predicted_rul = attribution_results['rul']
    sensor_impacts = attribution_results['sensor_impacts']
    
    # Get top k sensor impacts
    print(attribution_results)
    print(sensor_impacts)
    top_k_impacts = []
    for sensor, impact in list(sensor_impacts.items())[:k_most_effictive]:
        top_k_impacts.append({"sensor": sensor, "percent": round(impact * 100, 2)})

    print(top_k_impacts)
    return {"engine_number": engine_number,
            "predicted_rul": float(predicted_rul),
            "sensor_impacts": top_k_impacts}

    #predicted = predict_rul(model, seq_array_engine)

    #return {"engine_number": engine_number, "predicted_rul": predicted}


# @router.get("/engines_with_low_rul/")
# def get_engines_with_low_rul(threshold: float = 50.0):
#     """Find engines with RUL below threshold.
        
#         Example curl reqeust: 
#             curl `http://localhost:8000/api/predict/engines_with_low_rul/?threshold=10`
#     """
#     if model is None:
#         return {"error": "Model not loaded."}

#     low_rul_engines = []

#     for engine_number in lstm_test_df["unit_number"].unique():
#         engine_df = lstm_test_df[lstm_test_df["unit_number"] == engine_number]
#         if engine_df.empty:
#             continue

#         seq_array_engine = prepare_engine_sequence(engine_df, sequence_length, sequence_cols)
#         predicted = predict_rul(model, seq_array_engine)

#         if predicted < threshold:
#             low_rul_engines.append({"engine_number": int(engine_number), "predicted_rul": predicted})

#     return {"low_rul_engines": low_rul_engines}



@router.get("/engines_with_low_rul/")
def get_engines_with_low_rul(threshold: float = 50.0, until_clock: int = None):
    """Find engines with RUL below threshold, considering data up to a specific time.
    
    Args:
        threshold: RUL threshold below which engines are considered "low RUL"
        until_clock: Only use data up to this time cycle for prediction. 
                    If None, uses all available data.
        
    Example curl requests: 
        curl "http://localhost:8000/api/predict/engines_with_low_rul/?threshold=10"
        curl "http://localhost:8000/api/predict/engines_with_low_rul/?threshold=10&until_clock=50"
    """
    if model is None:
        return {"error": "Model not loaded."}

    low_rul_engines = []

    for engine_number in lstm_test_df["unit_number"].unique():
        # Filter by engine number
        engine_df = lstm_test_df[lstm_test_df["unit_number"] == engine_number]
        
        # Additional filter by time if until_clock is provided
        if until_clock is not None:
            # Assuming there's a time column (like 'time_cycles', 'cycle', etc.)
            # Replace 'time_cycles' with your actual time column name
            engine_df = engine_df[engine_df['time_in_cycles'] <= until_clock]
        
        if engine_df.empty:
            continue

        seq_array_engine = prepare_engine_sequence(engine_df, sequence_length, sequence_cols)
        predicted = predict_rul(model, seq_array_engine)

        if predicted < threshold:
            low_rul_engines.append({
                "engine_number": int(engine_number), 
                "predicted_rul": predicted,
                "data_until_clock": until_clock if until_clock is not None else "all"
            })

    return {
        "low_rul_engines": low_rul_engines,
        "result_number": len(low_rul_engines),
        "threshold": threshold,
        "until_clock": until_clock
    }

@router.post("/predict_new_engine_rul/", response_model=PredictionResponse)
def predict_new_engine_rul(engine_data: EngineData):
    """Predict RUL for new unseen engine data.
    
        Example curl request:
            `curl -X 'POST' \
                'http://localhost:8000/api/predict/predict_new_engine_rul/' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/json' \
                -d '{
                    "data": [
                        
                            [
                                0.0, 1.0, 0.545181, 0.310661, 0.269413, 0.652174, 0.212121,
                                0.127614, 0.208333, 0.646055, 0.220588, 0.308965, 0.333333,
                                0.55814, 0.661834, 0.0
                            ],
                            [
                                0.0, 2.0, 0.150602, 0.379551, 0.222316, 0.805153, 0.166667,
                                0.146684, 0.386905, 0.739872, 0.264706, 0.213159, 0.416667,
                                0.682171, 0.686827, 0.00277
                            ],
                            [
                                0.0, 3.0, 0.376506, 0.346632, 0.322248, 0.68599, 0.227273,
                                0.158081, 0.386905, 0.69936, 0.220588, 0.458638, 0.416667,
                                0.728682, 0.721348, 0.00554
                            ]
                        
                    ]
                }
                '
                `
    """
    if model is None:
        return {"error": "Model not loaded."}

    new_engine_sequence = np.asarray(engine_data.data).astype(np.float32)

    if new_engine_sequence.shape[1] != len(sequence_cols):
        return {
            "error": f"Input must have {len(sequence_cols)} features per time step."
        }

    # Pad/truncate
    num_elements = new_engine_sequence.shape[0]
    if num_elements < sequence_length:
        padding = np.zeros((sequence_length - num_elements, new_engine_sequence.shape[1]))
        processed_sequence = np.concatenate((padding, new_engine_sequence), axis=0)
    elif num_elements > sequence_length:
        processed_sequence = new_engine_sequence[-sequence_length:]
    else:
        processed_sequence = new_engine_sequence

    seq_array = np.asarray([processed_sequence]).astype(np.float32)
    predicted = predict_rul(model, seq_array)

    return {"predicted_rul": predicted}
