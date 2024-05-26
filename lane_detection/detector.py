import cv2
import numpy as np
from .preprocessor import preprocess_image
from .utils import draw_lane_lines

class LaneDetector:
    def __init__(self):
        pass

    def detect_lane(self, image):
        """
        Detect lanes in the input image.
        
        Args:
            image (numpy.ndarray): Input image.
            
        Returns:
            numpy.ndarray: Image with detected lanes drawn on it.
        """
        processed_image,mask = preprocess_image(image)
        lane_image = np.zeros_like(image)
        detected_image = cv2.addWeighted(image, 0.8, lane_image, 1, 1)
        
        return detected_image,mask

