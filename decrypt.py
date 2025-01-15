from cryptography.fernet import Fernet
import hashlib
import base64
import os

def decrypt_script():
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        custom_string = input("Enter Password: ")
        raw_key = hashlib.sha256(custom_string.encode()).digest()[:32]
        base64_key = base64.urlsafe_b64encode(raw_key)
        cipher_suite = Fernet(base64_key)
        f=input("Enter Filename:")
        fd="~/Desktop/"+f
        
        enpath = os.path.expanduser(fd)
        try:
            with open(enpath, "rb") as file:
                encrypted_code = file.read()
            decrypted_code = cipher_suite.decrypt(encrypted_code)
            print(decrypted_code.decode("utf-8"))
            print("Script executed successfully.")
            return 

        except Exception as e:
            attempts += 1
            print(f"Wrong password, you have {max_attempts - attempts} attempts left.")
            if attempts == max_attempts:
                print("Maximum attempts reached. Exiting.")
                break 

decrypt_script()
