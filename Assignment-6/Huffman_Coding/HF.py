#   from PIL import Image

# # Correct path to the image
# img = Image.open(r"E:\DIP\Huffman_Coding\Horse.jpg")

# # Display the image
# img.show()

from PIL import Image
import numpy as np
import heapq
import os

# Open and convert the image to grayscale

image = Image.open(r"E:\DIP\Huffman_Coding\Horse.jpg").convert('L')
pixels = np.array(image)




# Function to build a frequency dictionary
def build_frequency_dict(pixels):
    freq = {}
    for row in pixels:
        for pixel in row:
            if pixel in freq:
                freq[pixel] += 1
            else:
                freq[pixel] = 1
    return freq

# Huffman Node class
class HuffmanNode:
    def __init__(self, pixel_value, freq):
        self.pixel_value = pixel_value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman tree
def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(pixel, freq) for pixel, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        new_node = HuffmanNode(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(heap, new_node)

    return heap[0]

# Function to generate Huffman codes
def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.pixel_value is not None:
        codes[root.pixel_value] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Function to compress image using Huffman codes
def compress_image(pixels, codes):
    compressed_data = ""
    for row in pixels:
        for pixel in row:
            compressed_data += codes[pixel]
    return compressed_data

# Function to save compressed data to a file
def save_compressed_file(compressed_data, output_file):
    with open(output_file, 'wb') as f:
        f.write(compressed_data.encode())

# Main logic
freq_dict = build_frequency_dict(pixels)
huffman_tree = build_huffman_tree(freq_dict)
huffman_codes = generate_huffman_codes(huffman_tree)
compressed_data = compress_image(pixels, huffman_codes)

output_file = 'compressed_image.huff'
save_compressed_file(compressed_data, output_file)

print(f"Image compressed and saved as {output_file}")
