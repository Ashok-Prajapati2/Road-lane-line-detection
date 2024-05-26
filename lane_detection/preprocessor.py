import cv2
import numpy as np

def preprocess_image(image):
    """
    Preprocess the input image before lane detection.
    
    Args:
        image (numpy.ndarray): Input image.
        
    Returns:
        numpy.ndarray: Processed image.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([10, 90, 100])
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    mask_inverse = cv2.bitwise_not(mask)
    image[mask > 0] = (0, 255, 0)  # Green color

    # Display the result
    # cv2.imshow('Yellow to Green', image)
    
    return image,mask

