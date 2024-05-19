import matplotlib.pyplot as plt

def plot_sample(model, images, masks, num_samples=3):
    plt.figure(figsize=(10, 10))
    for i in range(num_samples):
        idx = np.random.randint(0, len(images))
        image = images[idx]
        mask = masks[idx]
        pred_mask = model.predict(image[np.newaxis, ...])[0]

        plt.subplot(num_samples, 3, i * 3 + 1)
        plt.imshow(image)
        plt.title('Input Image')

        plt.subplot(num_samples, 3, i * 3 + 2)
        plt.imshow(mask.squeeze(), cmap='gray')
        plt.title('True Mask')

        plt.subplot(num_samples, 3, i * 3 + 3)
        plt.imshow(pred_mask.squeeze(), cmap='gray')
        plt.title('Predicted Mask')

    plt.show()
