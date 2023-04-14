import numpy as np
import tensorflow as tf
from keras.models import Model

# Импорт параметров
# from utils.functions import config_reader

# config = config_reader()


class ModelSequential(Model):
    """Класс создаёт модель Sequential, наследуя класс от tf.keras.
    Параметры:
    ----------
    n_timesteps (_int_) - кол-во временных периодов
    n_channels (_int_) - кол-во датчиков
    output_units - 
    units - размерность модели из конфига 
    """    
    def __init__(self, X_train: np.ndarray, y_train: np.ndarray, units: int):

        super().__init__()
        # ------- параметры ------------
        self.n_timesteps = None
        #self.n_channels = X_train.shape[2]
        self.output_units = y_train.shape[-1]
        #self.units = units
                
        # -------- слои модели ----------------
        self.input_layer = x = tf.keras.layers.Input(shape=(self.n_timesteps, X_train.shape[1]))
        x = tf.keras.layers.Dropout(0.4)(x)
        
        x = tf.keras.layers.Dense(64, activation='relu')(x)
        x = tf.keras.layers.Dropout(0.4)(x)
        
        x = tf.keras.layers.Dense(32, activation='relu')(x)
        x = tf.keras.layers.Dropout(0.4)(x)
        
        x = tf.keras.layers.Dense(16, activation='relu')(x)
        x = tf.keras.layers.Dropout(0.4)(x)
        
        self.output_layer = tf.keras.layers.Dense(units=self.output_units, activation='sigmoid')(x)
        
        #print(f"input_shape = {(self.n_timesteps, self.n_channels)} | output_units = {self.output_units}")

    def build_model(self):
        """Метод формирования модели. 
        """
        model = tf.keras.Model(
            inputs=self.input_layer,
            outputs=self.output_layer,
            name="model_Sequential"
        ) 
        model.summary()
        return model