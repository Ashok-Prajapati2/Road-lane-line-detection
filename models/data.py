import os
import numpy as np
import cv2

def load_data(data_dir=r'/home/ashok/Desktop/github project/Road-lane-line-detection/models/dataset', img_size=(128, 128)):
    train_images = []
    train_masks = []
    val_images = []
    val_masks = []

    for phase in ['train', 'val']:
        img_dir = os.path.join(data_dir, phase, 'images')
        mask_dir = os.path.join(data_dir, phase, 'masks')

        for img_name in os.listdir(img_dir):
            img_path = os.path.join(img_dir, img_name)
            mask_path = os.path.join(mask_dir, img_name)

            if not os.path.isfile(img_path):
                print(f"Image file not found: {img_path}")
                continue
            if not os.path.isfile(mask_path):
                print(f"Mask file not found: {mask_path}")
                continue

            img = cv2.imread(img_path)
            if img is None:
                print(f"Failed to read image: {img_path}")
                continue
            img = cv2.resize(img, img_size)
            print(f"Loaded and resized image: {img_path} with shape {img.shape}")

            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            if mask is None:
                print(f"Failed to read mask: {mask_path}")
                continue
            mask = cv2.resize(mask, img_size)
            print(f"Loaded and resized mask: {mask_path} with shape {mask.shape}")

            if phase == 'train':
                train_images.append(img)
                train_masks.append(mask)
            else:
                val_images.append(img)
                val_masks.append(mask)

    train_images = np.array(train_images)
    train_masks = np.array(train_masks).reshape(-1, img_size[0], img_size[1], 1)
    val_images = np.array(val_images)
    val_masks = np.array(val_masks).reshape(-1, img_size[0], img_size[1], 1)

    print(f'Final train images shape: {train_images.shape}')
    print(f'Final train masks shape: {train_masks.shape}')
    print(f'Final validation images shape: {val_images.shape}')
    print(f'Final validation masks shape: {val_masks.shape}')

    return train_images, train_masks, val_images, val_masks

def preprocess_data(images, masks):
    images = images / 255.0
    masks = masks / 255.0
    return images, masks
