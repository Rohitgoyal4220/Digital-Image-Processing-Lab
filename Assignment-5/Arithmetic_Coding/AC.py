from PIL import Image
import numpy as np
import collections

# Function to perform arithmetic coding
def arithmetic_coding(frequencies, pixels):
    low = 0.0
    high = 1.0
    total_pixels = sum(frequencies.values())

    # Calculate cumulative frequencies
    cumulative_frequencies = {}
    cumulative_sum = 0
    for symbol, freq in sorted(frequencies.items()):
        cumulative_sum += freq
        cumulative_frequencies[symbol] = cumulative_sum / total_pixels

    # Encode the pixel values
    for pixel in pixels:
        range_width = high - low
        high = low + range_width * cumulative_frequencies[pixel]
        low = low + range_width * (cumulative_frequencies[pixel] - (frequencies[pixel] / total_pixels))

    # Scale the encoded value to an integer for storage
    scaled_encoded_value = int((low + high) / 2 * (2**64))  # Scale to a large integer

    return scaled_encoded_value

# Compress the image using arithmetic coding
def compress_image_arithmetic(image):
    # Flatten the image and calculate frequencies
    pixels = image.flatten()
    frequencies = collections.Counter(pixels)

    # Perform arithmetic coding
    encoded_value = arithmetic_coding(frequencies, pixels)

    # Save the frequencies and the encoded value to a file
    with open('compressed_image_arithmetic.bin', 'wb') as f:
        f.write(encoded_value.to_bytes(8, 'big'))  # Save the encoded value as bytes
        for pixel, freq in frequencies.items():
            f.write(f"{pixel}:{freq}\n".encode('utf-8'))  # Save pixel frequencies

    return frequencies

# Open the image and convert to grayscale
img = Image.open(r"E:\DIP\Huffman_Coding\Horse.jpg").convert('L')
pixels = np.array(img)

# Compress the image
frequencies = compress_image_arithmetic(pixels)
print("Image compressed and saved as 'compressed_image_arithmetic.bin'")
