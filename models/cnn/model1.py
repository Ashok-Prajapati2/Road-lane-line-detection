# models/cnn/mixed_attention_lane_model.py
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization, Activation, Add
from tensorflow.keras.layers import GlobalAveragePooling2D, Reshape, Dense, multiply

def residual_block(input_tensor, filters, kernel_size=3):
    # Main path
    x = Conv2D(filters, kernel_size, padding='same')(input_tensor)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    x = Conv2D(filters, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)

    # Shortcut path
    shortcut = Conv2D(filters, kernel_size=1, padding='same')(input_tensor)
    shortcut = BatchNormalization()(shortcut)

    # Add shortcut to main path
    x = Add()([x, shortcut])
    x = Activation('relu')(x)
    return x

def attention_module(input_tensor, filters):
    # Global average pooling
    gap = GlobalAveragePooling2D()(input_tensor)
    gap = Reshape((1, 1, filters))(gap)
    
    # Dense layers for attention
    attention = Dense(filters // 4, activation='relu')(gap)
    attention = Dense(filters, activation='sigmoid')(attention)
    
    # Multiply input tensor by attention weights
    multiplied = multiply([input_tensor, attention])
    return multiplied

def mixed_attention_lane_model(input_shape=(160, 576, 3)):
    inputs = Input(shape=input_shape)
    
    # Initial convolutional block
    x = Conv2D(64, (7, 7), strides=(2, 2), padding='same')(inputs)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    # Residual blocks with attention
    for filters in [64, 128, 256, 512]:
        x = residual_block(x, filters)
        x = attention_module(x, filters)
    
    # Final convolutional layer
    outputs = Conv2D(1, (1, 1), activation='sigmoid')(x)

    # Model construction
    model = Model(inputs=inputs, outputs=outputs)

    return model

# Instantiate and compile the model
lane_model = mixed_attention_lane_model()
lane_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model summary
lane_model.summary()
