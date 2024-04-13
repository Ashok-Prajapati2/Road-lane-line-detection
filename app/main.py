import sys
sys.path.insert(1, "/home/ashok/Desktop/github project/Road-lane-line-detection/")
import cv2
import os
from lane_detection.detector import LaneDetector
from app.gen_log import Logger
import time


def main():
    logger = Logger()
    logger.log_info('Starting lane detection...')

    detector = LaneDetector()

    test_image_path = 'data/test_images/example3.jpg'
    test_video_path = 'data/test_videos/example.mp4'

   # this code for image
    logger.log_info('Processing image...')
    image = cv2.imread(test_image_path)
    detected_image = detector.detect_lane(image)
    # cv2.imshow('Detected Lanes', detected_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    output_image_path = f'results/images/detected_lane{time.time()}.jpg'
    cv2.imwrite(output_image_path, detected_image)
    logger.log_info(f'Image processed and saved at: {output_image_path}')

    # for video
    cap = cv2.VideoCapture(test_video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(f'results/videos/detected_lane{time.time()}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        detected_frame = detector.detect_lane(frame)
        out.write(detected_frame)

    # cap.release()
    # out.release()
    cv2.destroyAllWindows()

    logger.log_info('Lane detection completed.')

if __name__ == "__main__":
    main()
