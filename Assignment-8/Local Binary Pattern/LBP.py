import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def local_binary_pattern(image, radius=1, points=8):
    # Get the dimensions of the image
    rows, cols = image.shape
    # Create an empty output image
    lbp_image = np.zeros((rows, cols), dtype=np.uint8)

    # Loop through each pixel in the image
    for i in range(radius, rows - radius):
        for j in range(radius, cols - radius):
            # Get the center pixel value
            center = image[i, j]
            binary_pattern = 0
            
            # Loop through the neighboring pixels
            for p in range(points):
                # Calculate the angle and the neighbor's coordinates
                theta = 2 * np.pi * p / points
                x = int(i + radius * np.sin(theta))
                y = int(j + radius * np.cos(theta))
                
                # Create the binary pattern
                if image[x, y] > center:
                    binary_pattern |= (1 << p)
                    
            lbp_image[i, j] = binary_pattern

    return lbp_image

# Load the image
img = Image.open(r"E:\DIP\Huffman_Coding\Horse.jpg").convert('L')  # Convert to grayscale
pixels = np.array(img)

# Compute the LBP
lbp_image = local_binary_pattern(pixels)

# Display the original image and the LBP image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(pixels, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Local Binary Pattern Image')
plt.imshow(lbp_image, cmap='gray')
plt.axis('off')

plt.show()
