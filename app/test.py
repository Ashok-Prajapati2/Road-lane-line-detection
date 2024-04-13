import sys
sys.path.insert(1, "/home/ashok/Desktop/github project/Road-lane-line-detection/")
import cv2
from lane_detection.detector import LaneDetector
from lane_detection.utils import draw_lane_lines as Utils
from models.cnn.model1 import mixed_attention_lane_model
from app.gen_log import Logger
import time
import os

def process_frame(frame, model):
    # Preprocess the frame
    preprocessed_frame = Utils.preprocess(frame)

    # Predict lane lines
    lane_lines = model.predict(preprocessed_frame)

    # Post-process the predictions to overlay on the original frame
    overlay_frame = Utils.overlay_lane_lines(frame, lane_lines)

    return overlay_frame

def main():
    # Initialize the lane detection model
    model = mixed_attention_lane_model()
    # Load the trained weights (make sure to train your model and update the path)
    model.load_weights('path_to_trained_model_weights.h5')

    # Start video capture
    cap = cv2.VideoCapture('path_to_video.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process each frame
        output_frame = process_frame(frame, model)

        # Display the frame with detected lane lines
        cv2.imshow('Lane Detection', output_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

    logger = Logger()
    logger.log_info('Starting lane detection...')

    detector = LaneDetector()

    test_image_path = 'data/test_images/example1.jpg'
    test_video_path = 'data/test_videos/example.mp4'

    # image proce
    logger.log_info('Processing image...')
    image = cv2.imread(test_image_path)
    detected_image = detector.detect_lane(image)
    cv2.imshow('Detected Lanes', detected_image)
    cv2.destroyAllWindows()
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

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    logger.log_info('Lane detection completed.')

if __name__ == "__main__":
    main()
