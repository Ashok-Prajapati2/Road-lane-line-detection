import albumentations as A

def augment_data(images, masks):
    aug = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
        A.Rotate(limit=15, p=0.5)
    ])

    augmented_images, augmented_masks = [], []
    for img, mask in zip(images, masks):
        augmented = aug(image=img, mask=mask)
        augmented_images.append(augmented['image'])
        augmented_masks.append(augmented['mask'])

    return np.array(augmented_images), np.array(augmented_masks)

if __name__ == "__main__":
    augmented_images, augmented_masks = augment_data(images, masks)
    print(f"Augmented {len(augmented_images)} images and {len(augmented_masks)} masks.")
