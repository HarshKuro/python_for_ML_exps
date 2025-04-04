#Write a file handeling progeram that will read, write, append the text in a file with the example of binary file (read, write)

import os
import struct 

with open('example.txt', 'w') as text_file:
    text_file.write("Hello, this is a text file.\n")
    text_file.write("This is the second line.\n")
    text_file.write("This is the third line.\n")
with open('example.txt', 'a') as text_file:
    text_file.write("This is the fourth line APPEND.\n")
with open('example.txt', 'r') as text_file:
    content = text_file.read()
    print("Content of the text file:")
    print(content)

binary_data = struct.pack('i', 12345)
with open('example.bin', 'wb') as binary_file:
    binary_file.write(binary_data)
with open('example.bin', 'rb') as binary_file:
    unpacked_data = struct.unpack('i', binary_file.read())
    print("Unpacked binary data:", unpacked_data[0])

# Writing a string to a binary file
string_data = "Hello, this is a string in a binary file."
encoded_data = string_data.encode('utf-8')  # Encode the string to bytes
with open('example2.bin', 'wb') as binary_file:
    binary_file.write(encoded_data)

# Reading the string back from the binary file
with open('example2.bin', 'rb') as binary_file:
    read_data = binary_file.read()
    decoded_data = read_data.decode('utf-8')  # Decode the bytes back to a string
    print("Decoded string from binary file:", decoded_data)

