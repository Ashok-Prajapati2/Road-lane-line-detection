import cv2
import numpy as np

def draw_lane_lines(image, lines, color=(0, 255, 0), thickness=5):
    """
    Draw lane lines on the input image.
    
    Args:
        image (numpy.ndarray): Input image.
        lines (list): List of lines in the format [[x1, y1, x2, y2], ...].
        color (tuple): Color of the lines in BGR format.
        thickness (int): Thickness of the lines.
    """
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)

