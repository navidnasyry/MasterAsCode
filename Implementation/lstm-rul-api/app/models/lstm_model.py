import pickle
import numpy as np
from app.core.utils import r2_keras
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer
from tensorflow.keras.models import load_model



class AttentionLayer(Layer):  # لایه سفارشی برای attention
    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        # input_shape should be (batch_size, time_steps, features)
        self.W = self.add_weight(name='att_weight', shape=(input_shape[-1], 1), initializer='random_normal', trainable=True)
        self.b = self.add_weight(name='att_bias', shape=(input_shape[1], 1), initializer='zeros', trainable=True)
        super(AttentionLayer, self).build(input_shape)

    def call(self, x):
        # x has shape (batch_size, time_steps, features)
        # محاسبه scores: e = tanh(W * x + b)
        e = K.tanh(K.dot(x, self.W) + self.b)
        # weights: alpha = softmax(e)
        alpha = K.softmax(e, axis=1)
        # context = sum(alpha * x)
        context = K.sum(alpha * x, axis=1)
        return context, alpha  # alpha = weights برای هر time-step/feature

def load_lstm_model(filepath='lstm_model'):
    """
    Load LSTM model and all necessary components, including saved sensor impacts
    """
    # Load the Keras model with custom objects
    # Ensure 'AttentionLayer' is correctly passed as a custom object
    model = load_model(
        f'{filepath}.h5',
        custom_objects={'r2_keras': r2_keras, 'AttentionLayer': AttentionLayer}
    )

    # Load the training history
    with open(f'{filepath}_history.pkl', 'rb') as f:
        history = pickle.load(f)

    # Load other components
    with open(f'{filepath}_data.pkl', 'rb') as f:
        model_data = pickle.load(f)

    print(f"LSTM model loaded successfully from {filepath}.h5")

    return model, history, model_data