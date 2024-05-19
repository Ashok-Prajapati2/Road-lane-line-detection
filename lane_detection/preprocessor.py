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
    # # Convert image to grayscale
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # # Apply Gaussian blur to reduce noise
    # blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # # Apply Canny edge detection
    # edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)
    
    # # Further preprocessing steps can be added here
    
    # De Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #find range of yellow color in HSV
    lower_yellow = np.array([10, 90, 100])
    upper_yellow = np.array([30, 255, 255])
    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Invert the mask to get regions where yellow is not present
    mask_inverse = cv2.bitwise_not(mask)

    # Replace yellow regions with green color
    image[mask > 0] = (0, 255, 0)  # Green color

    # Display the result
    # cv2.imshow('Yellow to Green', image)
    
    return image

