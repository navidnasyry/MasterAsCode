from tensorflow.keras import backend as K

def r2_keras(y_true, y_pred):
    """Coefficient of Determination (R²) for Keras."""
    SS_res = K.sum(K.square(y_true - y_pred))
    SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
    return 1 - SS_res / (SS_tot + K.epsilon())
