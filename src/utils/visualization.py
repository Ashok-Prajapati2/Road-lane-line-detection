import matplotlib.pyplot as plt

def visualize_results(images, masks, predictions, index):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.title('Image')
    plt.imshow(images[index])

    plt.subplot(1, 3, 2)
    plt.title('Mask')
    plt.imshow(masks[index], cmap='gray')

    plt.subplot(1, 3, 3)
    plt.title('Prediction')
    plt.imshow(predictions[index], cmap='gray')

    plt.show()

if __name__ == "__main__":
    import numpy as np
    images = np.random.rand(10, 256, 256, 3)
    masks = np.random.randint(0, 2, (10, 256, 256, 1))
    predictions = np.random.rand(10, 256, 256, 1)
    visualize_results(images, masks, predictions, index=0)
