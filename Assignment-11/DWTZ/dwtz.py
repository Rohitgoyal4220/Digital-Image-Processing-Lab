import numpy as np
import pywt
import matplotlib.pyplot as plt
from PIL import Image

def dwt2d(image_path):
    # Load the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img_array = np.array(img)

    # Perform 2D DWT
    coeffs2 = pywt.dwt2(img_array, 'haar')  # You can choose other wavelets like 'db1', 'sym2', etc.
    cA, (cH, cV, cD) = coeffs2

    # Plotting the results
    plt.figure(figsize=(12, 8))
    
    plt.subplot(221)
    plt.imshow(cA, interpolation="nearest", cmap='gray')
    plt.title('Approximation Coefficients (cA)')
    plt.axis('off')

    plt.subplot(222)
    plt.imshow(cH, interpolation="nearest", cmap='gray')
    plt.title('Horizontal Detail Coefficients (cH)')
    plt.axis('off')

    plt.subplot(223)
    plt.imshow(cV, interpolation="nearest", cmap='gray')
    plt.title('Vertical Detail Coefficients (cV)')
    plt.axis('off')

    plt.subplot(224)
    plt.imshow(cD, interpolation="nearest", cmap='gray')
    plt.title('Diagonal Detail Coefficients (cD)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Example usage
image_path = r"E:\DIP\Huffman_Coding\Horse.jpg"  # Update this path to your image
dwt2d(image_path)
