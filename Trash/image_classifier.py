import tensorflow as tf
from tensorflow import keras
import numpy as np

# Trying to build an image classifier
# Keep getting NaN loss values :(

def create_model():
    """Create a simple CNN model"""
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        # TODO: add more layers? Not sure how many
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # TODO: is this the right optimizer?
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def load_data():
    """Load and preprocess data"""
    # Using MNIST for now
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    # Normalize - should this be 255.0 or 255?
    x_train = x_train / 255.0
    x_test = x_test / 255.0
    
    # Reshape
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    
    return (x_train, y_train), (x_test, y_test)

def train_model(model, x_train, y_train):
    """Train the model"""
    # TODO: add validation split
    # TODO: add callbacks for early stopping
    
    history = model.fit(
        x_train, 
        y_train,
        epochs=5,  # should this be more?
        batch_size=32
        # validation_data=(x_test, y_test)  # this causes errors
    )
    
    return history

if __name__ == "__main__":
    model = create_model()
    (x_train, y_train), (x_test, y_test) = load_data()
    
    # train_model(model, x_train, y_train)  # commented out - model not converging
    
    # TODO: save model
    # TODO: evaluate on test set
