import zipfile
import os

# Define the name of the zip file and the text file
zip_filename = 'protected.zip'
txt_filename = 'payload.txt'
password = 'zzzzzzzzzz'

# Create a text document
with open(txt_filename, 'w') as file:
    file.write('This is the hidden message')

# Create a zip file
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(txt_filename)

# Encrypt the zip file (assuming the `zip` command is available)
os.system(f'zip -P {password} {zip_filename} {txt_filename}')

print(f'Created {zip_filename} with a password-protected text document.')
os.unlink(txt_filename)