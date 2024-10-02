import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def load_images_from_folder(folder_path):
    images = []
    labels = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path).convert('L')  # Convert to grayscale
            img = img.resize((32, 32))  # Resize images to a uniform size
            images.append(np.array(img).flatten())  # Flatten the image array
            labels.append(filename)  # Store the filename as label
    return np.array(images), np.array(labels)

# Load dataset
folder_path = r"E:\DIP\images"  # Update this to your folder containing images
X, y = load_images_from_folder(folder_path)

# Choose the number of clusters
num_clusters = 3  # You can change this value based on your requirement

# Create and fit the K-Means model
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Predict the clusters
clusters = kmeans.predict(X)

# Plotting the clustered images
for i in range(num_clusters):
    plt.figure(figsize=(10, 5))
    plt.title(f'Cluster {i + 1}')
    
    # Get indices of images in the current cluster
    cluster_indices = np.where(clusters == i)[0]
    
    # Plot the images in the current cluster
    for j, idx in enumerate(cluster_indices[:5]):  # Show up to 5 images per cluster
        plt.subplot(1, 5, j + 1)
        plt.imshow(X[idx].reshape(32, 32), cmap='gray')
        plt.axis('off')
        plt.title(y[idx])  # Use the filename as title

    plt.show()
