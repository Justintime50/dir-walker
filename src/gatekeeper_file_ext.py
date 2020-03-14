"""Search for files with a specific extension in the specified directory"""
import os

# Define variables
DIR = "./"
EXT = ".py"

# Run script
for root, dirs, files in os.walk(DIR):
    for file in files:
        if file.endswith(EXT):
            print(os.path.join(root, file))
