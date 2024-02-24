import os
import argparse
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_image(input_file, output_file):
    # Generate a random key
    key = get_random_bytes(16)
    
    # Initialize AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Read the input image file
    with open(input_file, 'rb') as f:
        image_data = f.read()
    
    # Pad the image data to be a multiple of 16 bytes
    padded_data = pad(image_data, AES.block_size)
    
    # Encrypt the padded image data
    encrypted_data = cipher.encrypt(padded_data)
    
    # Write the encrypted data and key to the output file
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    
    return key

def decrypt_image(input_file, output_file, key):
    # Initialize AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Read the encrypted data from the input file
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Decrypt the encrypted data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt PNG, JPG, JPEG images")
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help="Action to perform: encrypt or decrypt")
    parser.add_argument('input_file', help="Input image file")
    parser.add_argument('output_file', help="Output image file")
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.input_file):
        print("Error: Input file does not exist")
        return
    
    # Perform encryption or decryption based on the action
    if args.action == 'encrypt':
        key = encrypt_image(args.input_file, args.output_file)
        print("Image encrypted successfully.")
        print("Key:", key.hex())
    elif args.action == 'decrypt':
        key_hex = input("Enter the key to decrypt the image: ")
        try:
            key = bytes.fromhex(key_hex)
            decrypt_image(args.input_file, args.output_file, key)
            print("Image decrypted successfully.")
        except ValueError:
            print("Error: Invalid key format")

if __name__ == "__main__":
    main()
