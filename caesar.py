from encrypt import encrypt
from decrypt import decrypt
def caesar():
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt - ").lower()
    text = input("Enter Message : ").lower()
    shift = int(input("Enter Shift Amount : "))
    if direction == "encode":
        print(encrypt(text, shift))
    elif direction == "decode":
        print(decrypt(text, shift))
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")