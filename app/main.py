import sys
sys.path.insert(1,r"/home/ashok/Desktop/github project/Road-lane-line-detection")
import cv2
import os
from lane_detection.detector import LaneDetector
from app.gen_log import Logger
import time
from models.train import train_model
from models.evaluate import evaluate_model

def main():
    logger = Logger()
    logger.log_info('Starting lane detection...')

    try:
        # Initialize lane detector
        detector = LaneDetector()
    except Exception as e:
        logger.log_error(f"Error initializing lane detector: {e}")
        return

    # Set test image and video paths
    test_image_path = f'data/images/example5.jpg'
    test_video_path = 'data/test_videos/example00.mp4'

    # Process image
    logger.log_info('Processing image...')
    image = cv2.imread(test_image_path)
    if image is None:
        logger.log_error("Failed to load the test image.")
        return

    # Detect lanes in image
    detected_image, masks = detector.detect_lane(image)

    # Save detected image and mask
    output_image_path = f'results/images/detected_lane.jpg'
    output_mask_path = f'results/masks/detected_lane_mask.png'
    cv2.imwrite(output_mask_path, masks)
    cv2.imwrite(output_image_path, detected_image)
    logger.log_info(f'Image processed and saved at: {output_image_path}')

    # Process video
    logger.log_info('Processing Video...')
    try:
        # Initialize video capture
        cap = cv2.VideoCapture(test_video_path)
        if not cap.isOpened():
            logger.log_error("Error opening video file.")
            return

        # Get video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Initialize video writer
        output_video_path = f'results/videos/detected_lane{time.time()}.mp4'
        out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

        # Process video frames
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect lanes in frame
            detected_frame = detector.detect_lane(frame)

            # Write detected frame to video
            out.write(detected_frame)

        logger.log_info(f'Video  processed and saved at: {output_video_path }')
        logger.log_info('Lane detection completed.')
    except Exception as e:
        logger.log_error(f"Error processing video: {e}")

    # Print log file
    try:
        log_file_path = logger.get_log_file_path()
        with open(log_file_path, 'r') as log_file:
            print(log_file.read())
    except Exception as e:
        print(f"Error reading log file: {e}")

    # Train and evaluate model
    data_path = 'data/'
    model_save_path = 'models/lane_detection_model.keras'
    train_model(data_path, model_save_path)
    evaluate_model(data_path, model_save_path)
    cv2.destroyAllWindows()

# Run main function
if __name__ == "__main__":
    main()