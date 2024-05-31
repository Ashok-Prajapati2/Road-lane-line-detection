import sys
import cv2
import os
try:
    path = os.getcwd()
    sys.path.insert(1,path)
except Exception as e:
    print("Error in adding path",e)

from lane_detection.detector import LaneDetector
from app.gen_log import Logger
import time


def main():
    logger = Logger()
    logger.log_info('Starting lane detection...')

    try:
        detector = LaneDetector()
    except Exception as e:
        logger.log_error(f"Error initializing lane detector: {e}")
        return

    test_image_path = 'data/test_images/example5.jpg'
    test_video_path = 'data/test_videos/example1.mp4'

    # Process image
    logger.log_info('Processing image...')
    image = cv2.imread(test_image_path)
    if image is None:
        logger.log_error("Failed to load the test image.")
        return

    try:
        detected_image, mask = detector.detect_lane(image)
        output_image_path = 'results/images/detected_lanet.jpg'
        cv2.imwrite(output_image_path, detected_image)
        logger.log_info(f'Image processed and saved at: {output_image_path}')

        output_mask_path = 'results/masks/detected_lane_mask.jpg'
        cv2.imwrite(output_mask_path, mask)
        logger.log_info(f'Image processed and saved at: {output_mask_path}')
    except Exception as e:
        logger.log_error(f"Error processing image: {e}")
        return

    # Process video
    logger.log_info('Processing Video...')
    try:
        cap = cv2.VideoCapture(test_video_path)
        if not cap.isOpened():
            logger.log_error("Error opening video file.")
            return

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        output_video_path = f'results/videos/detected_lane_{time.time()}.mp4'
        output_mask_video_path = f'results/videos/detected_lane_mask_{time.time()}.mp4'
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
        out_mask = cv2.VideoWriter(output_mask_video_path, fourcc, fps, (frame_width, frame_height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            try:
                detected_frame, mask = detector.detect_lane(frame)
                out.write(detected_frame)
                out_mask.write(mask)
            except Exception as e:
                logger.log_error(f"Error processing frame: {e}")

        cap.release()
        out.release()
        out_mask.release()
        logger.log_info(f'Video processed and saved at: {output_video_path}')
        logger.log_info(f'Mask video processed and saved at: {output_mask_video_path}')
        logger.log_info('Lane detection completed.')
    except Exception as e:
        logger.log_error(f"Error processing video: {e}")
    finally:
        cv2.destroyAllWindows()

    try:
        log_file_path = logger.get_log_file_path()
        with open(log_file_path, 'r') as log_file:
            print(log_file.read())
    except Exception as e:
        print(f"Error reading log file: {e}")

if __name__ == "__main__":
    main()
