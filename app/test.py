import numpy as np
from sklearn.model_selection import train_test_split

# Generate random features and labels for demonstration
num_samples = 10
num_features = 2

# Generate random features (slope and intercept)
X_data = np.random.rand(num_samples, num_features)

# Generate random labels (1 for lane, 0 for non-lane)
y_data = np.random.randint(2, size=num_samples)

print(X_data)
print(y_data)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

# Display the shapes of training and testing sets
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Display testing data
print("Testing data:")
for i in range(len(X_test)):
    print("Features:", X_test[i], "Label:", y_test[i])
