import tensorflow as tf
from data import load_data, preprocess_data
from model import build_unet
from utils import plot_sample

# Load and preprocess data
train_images, train_masks, val_images, val_masks = load_data()
train_images, train_masks = preprocess_data(train_images, train_masks)
val_images, val_masks = preprocess_data(val_images, val_masks)

# Check the shapes of the data
print(f'Train images shape: {train_images.shape}')
print(f'Train masks shape: {train_masks.shape}')
print(f'Validation images shape: {val_images.shape}')
print(f'Validation masks shape: {val_masks.shape}')

Ensure the data is in the correct shape
assert train_images.shape[1:] == (128, 128, 3), "Train images shape is incorrect"
assert train_masks.shape[1:] == (128, 128, 1), "Train masks shape is incorrect"
assert val_images.shape[1:] == (128, 128, 3), "Validation images shape is incorrect"
assert val_masks.shape[1:] == (128, 128, 1), "Validation masks shape is incorrect"

# Build the model
model = build_unet(input_shape=(128, 128, 3))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(train_images, train_masks, validation_data=(val_images, val_masks), epochs=50, batch_size=16)

# Save the model
model.save('results/model.h5')

# Plot sample predictions
plot_sample(model, val_images, val_masks)
