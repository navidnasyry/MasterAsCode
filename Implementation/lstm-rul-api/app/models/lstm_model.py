import pickle
import numpy as np
from tensorflow.keras.models import load_model
from app.core.utils import r2_keras


def load_lstm_model(filepath: str):
    """Load trained LSTM model and metadata."""
    model = load_model(f"{filepath}.h5", custom_objects={'r2_keras': r2_keras})

    with open(f"{filepath}_history.pkl", "rb") as f:
        history = pickle.load(f)

    with open(f"{filepath}_data.pkl", "rb") as f:
        model_data = pickle.load(f)

    print(f"✅ LSTM model loaded from {filepath}.h5")
    return model, history, model_data
