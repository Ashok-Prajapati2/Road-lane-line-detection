import sys
import os
sys.path.insert(1,r"/home/ashok/Desktop/github project/Road-lane-line-detection/src/")
sys.path.insert(1,r"/home/ashok/Desktop/github project/Road-lane-line-detection")
import numpy as np
from tensorflow.keras.models import load_model
from data_loader import load_data
from preprocess import preprocess_data
from utils.metrics import iou_metric

def evaluate_model(data_path, model_path):
    images, masks = load_data(data_path)
    images, masks = preprocess_data(images, masks)

    model = load_model(model_path, compile=False)
    predictions = model.predict(images)

    iou = iou_metric(masks, predictions)
    print(f"Mean IoU: {iou:.4f}")


if __name__ == "__main__":
    data_path = '/data'
    model_path = '/models/lane_detection_model.keras'
    evaluate_model(data_path, model_path)