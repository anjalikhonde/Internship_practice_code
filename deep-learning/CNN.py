import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras import Input
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the images
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape the images for CNN
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Build the CNN model
model = Sequential()

model.add(Input(shape=(28, 28, 1)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)

print(f"\nTest Accuracy: {accuracy * 100:.2f}%")

# Predict on the test dataset
predictions = model.predict(x_test)

# Display the first test image
plt.imshow(x_test[0, :, :, 0], cmap='gray')
plt.title("Test Image")
plt.axis('off')
plt.show()

# Print actual and predicted digit
print("Actual Digit    :", y_test[0])
print("Predicted Digit :", predictions[0].argmax())

# Save the trained model
model.save("mnist_cnn.keras")

print("\nModel saved successfully as 'mnist_cnn.keras'")