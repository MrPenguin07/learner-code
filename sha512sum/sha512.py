'''
A simple interactive python script to hash a sha512 string, print hash of and/or verify a local file to a known hash.
'''
import hashlib
import os
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit import prompt

def hash_string(string):
    return hashlib.sha512(string.encode()).hexdigest()

def hash_file(file_path):
    BLOCK_SIZE = 65536  # The size of each read from the file
    file_hash = hashlib.sha512()  # Create the hash object, using the SHA-512 algorithm
    with open(file_path, 'rb') as f:  # Open the file in binary mode
        fb = f.read(BLOCK_SIZE)  # Read the file in blocks
        while len(fb) > 0:
            file_hash.update(fb)  # Update the hash object with the block of data
            fb = f.read(BLOCK_SIZE)  # Read the next block of data
    return file_hash.hexdigest()  # Return the hexadecimal representation of the hash

def verify_file(file_path, known_hash):
    calculated_hash = hash_file(file_path)
    if calculated_hash == known_hash:
        print("The file has been verified. Hash MATCH: ", calculated_hash)
    else:
        print("The file could NOT be verified. Hash MISMATCH. Calculated hash: ", calculated_hash)

while True:
    choice = input("Enter 's' to hash a string, 'f' to get the sum of a file, 'v' to verify a file (or 'q' to quit): ")
    if choice == 'q':
        break
    elif choice == 's':
        string_to_hash = input("Enter a string to hash: ")
        hashed_string = hash_string(string_to_hash)
        print("Hashed string: ", hashed_string)
    elif choice == 'f':
        file_path = prompt("Enter the path to file: ", completer=PathCompleter())
        if os.path.isfile(file_path):
            hashed_string = hash_file(file_path)
            print("Hashed string: ", hashed_string)
        else:
            print("Invalid file name or path. Please try again.")
    elif choice == 'v':
        file_path = prompt("Enter the path to file: ", completer=PathCompleter())
        if os.path.isfile(file_path):
            known_hash = input("Enter the known hash: ")
            verify_file(file_path, known_hash)
        else:
            print("Invalid file name or path. Please try again.")
    else:
        print("Invalid choice. Please enter 's' to hash a string, 'f' to hash a file, 'v' to verify a file or 'q' to quit.")
