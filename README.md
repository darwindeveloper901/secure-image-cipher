# SecureImageCipher 🖼️

SecureImageCipher is a Python CLI tool that allows you to encrypt and decrypt PNG, JPG, and JPEG images into gibberish images, providing you with a key to unlock them later. This gives you complete control over the security of your images.

## Features 🛡️

- Encrypts and decrypts PNG, JPG, and JPEG images.
- Provides a unique key for each encryption to ensure secure decryption.
- Ensures complete control and security over your images.

## Usage 🚀

1. To encrypt an image:
    ```bash
    python image-cipher encrypt <image_path>
    ```

2. To decrypt an image:
    ```bash
    python image-cipher decrypt <encrypted_image_path> <key>
    ```

## Requirements 📋

- Python 3.x
- Pillow library (install using `pip install Pillow`)

## Notes 📝

- Ensure to keep your encryption keys secure as they are needed for decryption.
- This tool is for personal use and should not be used for illegal activities.

