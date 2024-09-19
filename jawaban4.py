import heapq
from collections import defaultdict, Counter

# Node class untuk Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # membandingkan node (prioritas)
    def __lt__(self, other):
        return self.freq < other.freq

# membuat Huffman Tree
def huffmanTree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# menghasilkan Huffman Codes dari Huffman Tree
def generate_huffman_codes(root, prefix="", code_map={}):
    if root is None:
        return

    # jika simpul daun, tambahkan karakter dan kodenya
    if root.char is not None:
        code_map[root.char] = prefix

    generate_huffman_codes(root.left, prefix + "0", code_map)
    generate_huffman_codes(root.right, prefix + "1", code_map)

    return code_map

# mengodekan teksnya
def huffman_encoding(text, code_map):
    encoded_text = "".join([code_map[char] for char in text])
    return encoded_text

# menghitung frekuensi karakter dalam teks
def calculate_frequencies(text):
    return Counter(text)

# fungsi untuk menangani Huffman Compression
def huffman_compress(text):
    frequencies = calculate_frequencies(text)
    huffman_tree = huffmanTree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    encoded_text = huffman_encoding(text, huffman_codes)
    
    # menampilkan hasil
    print("Huffman Codes untuk setiap karakter:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
    
    print(f"\nOriginal text: {text}")
    print(f"Text code: {encoded_text}")
    
    # menhitung rasio kompresi
    original_size = len(text) * 8  # asumsi 8-bit per karakter
    compressed_size = len(encoded_text)
    compression_ratio = (original_size - compressed_size) / original_size
    
    print(f"\nUkuran original: {original_size} bits")
    print(f"Ukuran kompresi: {compressed_size} bits")
    print(f"Rasio kompresi: {compression_ratio * 100:.2f} %")

if __name__ == "__main__":
    # teks: INSAN UNGGUL ​​JAYA
    text = "INSAN UNGGUL JAYA"
    huffman_compress(text)
