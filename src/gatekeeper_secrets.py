"""Search files for secrets such as passwords, API keys, etc"""
import re
import os
import sys

# Define some variables
DIR = sys.argv[1] # Alternatively you could specify the explicit path here
LENGTH = "16"

print("\n##########\nGATEKEEPER\n##########\n")
print("The following files in the specified directory may have secrets stored in them:\n")
REGEX = re.compile(r"\b\w{" + re.escape(LENGTH) + r",}\b")
GITIGNORE = open(os.path.join(DIR, '.gitignore'), 'r').read().splitlines()

# Run script iterating over each file and directory
for root, dirs, files in os.walk(DIR):
    if '.git' in dirs:
        dirs.remove('.git')
    # Open each file and check for secrets
    for file in files:
        if file in GITIGNORE:
            continue
        filepath = os.path.join(root, file)
        with open(filepath, "r") as single_file:

            # Print the data
            for line_number, line in enumerate(single_file, 1):
                data = REGEX.findall(line)
                for secret in data:
                    print("File: " + filepath)
                    print("Secret: " + secret)
                    print("Line: " + "%d\n" % line_number)
