import pyzipper
import os

def unzip_folder_with_password(zip_path, extract_to, password):
    # Open the encrypted zip file
    with pyzipper.AESZipFile(zip_path, 'r') as zip_file:
        # Set the password
        zip_file.pwd = password.encode('utf-8')
        
        # Extract all the files
        zip_file.extractall(path=extract_to)

# Paths and password
zip_file_path = "Code.zip"
extract_to_folder = "."
password = os.environ.get('Passkey')

# Extract the zip file
unzip_folder_with_password(zip_file_path, extract_to_folder, password)

print("Zip file successfully extracted.")