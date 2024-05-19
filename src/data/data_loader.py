
import os
import cv2
import numpy as np

def load_data(data_path, img_size=(256, 256)):
    images, masks = [], []
    images_path = os.path.join(data_path, 'images')
    masks_path = os.path.join(data_path, 'masks')
    
    for img_file in os.listdir(images_path):
        img = cv2.imread(os.path.join(images_path, img_file))
        if img is None:
            print(f"Warning: Image {img_file} not loaded correctly.")
            continue
        
        img = cv2.resize(img, img_size)
        images.append(img)

        mask_file = img_file.replace('.jpg', '_mask.png')
        mask = cv2.imread(os.path.join(masks_path, mask_file), 0)
        if mask is None:
            print(f"Warning: Mask {mask_file} not loaded correctly.")
            continue
        
        mask = cv2.resize(mask, img_size)
        masks.append(mask)

    return np.array(images), np.array(masks)

if __name__ == "__main__":
    images, masks = load_data('../data/raw')
    print(f"Loaded {len(images)} images and {len(masks)} masks.")
