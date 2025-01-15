# File Encryption and Decryption with AES-GCM (Fernet)

This project provides Python scripts to encrypt and decrypt files securely using AES-GCM encryption via the `cryptography` library.

## Features
- **Symmetric Encryption**: Uses AES-GCM encryption (via `Fernet`) for secure file encryption.
- **Password-Based Key Derivation**: SHA-256 hash is used to derive a 256-bit key from a password.
- **Cross-Platform**: Works on any platform where Python is installed.
- **Complete Solution**: Includes both encryption and decryption scripts.

## Prerequisites
- Python 3.6 or higher
- Install dependencies:
  ```bash
  pip install -r requirements.txt
