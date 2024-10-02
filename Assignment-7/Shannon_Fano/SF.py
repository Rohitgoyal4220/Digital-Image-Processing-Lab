from PIL import Image
import numpy as np
import collections

# Function to generate Shannon-Fano codes
def shannon_fano(frequencies):
    sorted_freq = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    def recursive_shannon_fano(freq_list):
        if len(freq_list) == 1:
            return {freq_list[0][0]: ""}
        total_freq = sum(f[1] for f in freq_list)
        cumulative_freq = 0
        split_idx = 0
        
        # Find the split point
        for i in range(len(freq_list)):
            cumulative_freq += freq_list[i][1]
            if cumulative_freq >= total_freq / 2:
                split_idx = i + 1
                break

        # Recursively assign binary codes
        left_codes = recursive_shannon_fano(freq_list[:split_idx])
        right_codes = recursive_shannon_fano(freq_list[split_idx:])
        
        # Add 0 to the left and 1 to the right
        codes = {}
        for symbol, code in left_codes.items():
            codes[symbol] = '0' + code
        for symbol, code in right_codes.items():
            codes[symbol] = '1' + code
        
        return codes

    return recursive_shannon_fano(sorted_freq)

# Compress the image using Shannon-Fano coding
def compress_image_shannon_fano(image):
    # Flatten the image and calculate frequencies
    pixels = image.flatten()
    frequencies = collections.Counter(pixels)
    
    # Generate Shannon-Fano codes
    shannon_fano_codes = shannon_fano(frequencies)
    
    # Create the compressed binary string
    compressed_data = "".join([shannon_fano_codes[pixel] for pixel in pixels])
    
    # Convert binary string to bytes and save to file
    with open('compressed_image_shannon_fano.huff', 'wb') as f:
        byte_array = bytearray()
        for i in range(0, len(compressed_data), 8):
            byte = compressed_data[i:i + 8]
            byte_array.append(int(byte, 2))
        f.write(byte_array)
    
    return shannon_fano_codes

# Open the image and convert to grayscale
img = Image.open(r"E:\DIP\Huffman_Coding\Horse.jpg").convert('L')
pixels = np.array(img)

# Compress the image
shannon_fano_codes = compress_image_shannon_fano(pixels)
print("Image compressed and saved as 'compressed_image_shannon_fano.huff'")
