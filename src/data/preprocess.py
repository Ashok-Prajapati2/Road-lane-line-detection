import cv2
import numpy as np

def preprocess_data(images, masks, img_size=(256, 256)):
    processed_images, processed_masks = [], []
    for img, mask in zip(images, masks):
        img = cv2.resize(img, img_size)
        mask = cv2.resize(mask, img_size)
        processed_images.append(img)
        processed_masks.append(mask)

    return np.array(processed_images), np.array(processed_masks)

if __name__ == "__main__":
    images, masks = preprocess_data(images, masks)
    print(f"Preprocessed {len(images)} images and {len(masks)} masks.")
