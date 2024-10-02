import numpy as np
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

def load_images_from_folder(folder_path):
    images = []
    labels = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path).convert('L')  # Convert to grayscale
            img = img.resize((32, 32))  # Resize images to a uniform size
            images.append(np.array(img).flatten())  # Flatten the image array
            label = filename.split('_')[0]  # Assuming the label is the prefix before the underscore
            labels.append(label)
    return np.array(images), np.array(labels)

# Load dataset
folder_path = r"E:\DIP\images"  # Update this to your folder containing images
X, y = load_images_from_folder(folder_path)

# Check if there are enough images
if len(X) < 3:
    raise ValueError("Need at least 3 samples to use KNN with n_neighbors=3.")

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=1)  # Change to 1 if you have very few samples
knn.fit(X_train, y_train)

# Make predictions
if len(X_test) > 0:  # Check to ensure there are test samples
    y_pred = knn.predict(X_test)

    # Evaluate the model
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Optional: Display a sample image and its prediction
    sample_index = 0
    plt.imshow(X_test[sample_index].reshape(32, 32), cmap='gray')
    plt.title(f'Predicted: {y_pred[sample_index]}')
    plt.axis('off')
    plt.show()
else:
    print("No test samples available for prediction.")
