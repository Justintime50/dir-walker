"""Search files for secrets such as passwords, API keys, etc"""
import re
import os

# Define some variables
DIR = "./"
# TODO: Make LENGTH a variable here

# Run script
print("The following files in the specified directory may have secrets stored in code:")
for root, dirs, files in os.walk(DIR):
    for FILE in files:
        SINGLEFILE = open(FILE, "r")
        regex = re.compile(r"\b\w{12,}\b")
        for line in SINGLEFILE:
            data = regex.findall(line)
            for secret in data:
                print(os.path.join(root, FILE, secret)) # TODO: Print line numbers here
