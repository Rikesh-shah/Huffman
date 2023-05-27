from huffman import HuffmanCoding
import sys

path = "sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("compressed file path: "+output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path:"+decom_path)