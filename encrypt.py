from cryptography.fernet import Fernet
import hashlib
import base64
import os

# Step 1: Use the password to derive the key
password = input("Enter the password to encrypt: ")

# Derive the key from the password
raw_key = hashlib.sha256(password.encode()).digest()[:32]

# Base64 encode the key to match Fernet's requirements
base64_key = base64.urlsafe_b64encode(raw_key)

# Initialize the Fernet cipher suite
cipher_suite = Fernet(base64_key)

# Read the file to encrypt
f=input("Enter Filename:")
fd="~/Desktop/"+f
file_path = os.path.expanduser(fd)
with open(file_path, "rb") as file:
    file_data = file.read()

# Encrypt the file data
encrypted_data = cipher_suite.encrypt(file_data)

# Save the encrypted file
d=input("Enter New File Name:")
dd="~/Desktop/"+d
encrypted_file_path = os.path.expanduser(dd)
with open(encrypted_file_path, "wb") as file:
    file.write(encrypted_data)

print(f"File encrypted and saved as {encrypted_file_path}")
