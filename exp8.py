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


#WAP to handle 0 division, value and index error using exception handling         2nd part of the task
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    return result
def value_error(value):
    try:
        value = int(value)
    except ValueError:
        print("Error: Invalid value. Please enter a number.")
        return None
    return value
def index_error(lst, index):
    try: 
        value = lst[index]
    except IndexError:
        print("Error: Index out of range.")
        return None
    else:
        return value

#exapmple usage
print("Division Example:")
print(divide(10, 0))  # Division by zero
print(divide(10, 2))  # Valid division

print("\nValue Error Example:")
print(value_error("abc"))  # Invalid value
print(value_error("123"))  # Valid value

print("\nIndex Error Example:")
print(index_error([1, 2, 3], 5))  # Index out of range
print(index_error([1, 2, 3], 1))  # Valid index


#WAP to print the multiplication table of any given number using use try, except and finally block
# WAP to print the multiplication table of any given number using try, except, and finally block

def print_multiplication_table():
    try:
        number = int(input("Enter a number to print its multiplication table: "))
        print(f"Multiplication table for {number}:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Error: Please enter a valid integer.")
    finally:
        print("Execution of the multiplication table program is complete.")

# Example usage
print_multiplication_table()





