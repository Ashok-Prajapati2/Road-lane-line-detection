import sys
import os

sys.path.insert(1,r"/home/ashok/Desktop/github project/Road-lane-line-detection")
sys.path.insert(1,r"/home/ashok/Desktop/github project/Road-lane-line-detection/src/data")

import numpy as np
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.optimizers import Adam
from .model import unet_vgg16
from data_loader import load_data
from preprocess import preprocess_data

def train_model(data_path, model_save_path):
    images, masks = load_data(data_path)
    images, masks = preprocess_data(images, masks)

    model = unet_vgg16(input_shape=(256, 256, 3))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

    checkpoint = ModelCheckpoint(model_save_path, monitor='val_loss', save_best_only=True)
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    model.fit(images, masks, validation_split=0.2, epochs=50, batch_size=16, callbacks=[checkpoint, early_stopping])

if __name__ == "__main__":
    train_model('/data', 'models/lane_detection_model.keras')
