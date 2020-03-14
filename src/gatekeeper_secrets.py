"""Search files for secrets such as passwords, API keys, etc"""
import re
import os
import sys

# Define some variables
DIR = sys.argv[1] # Alternatively you could specify the explicit path here
LENGTH = "16"

print("\nGATEKEEPER\n")
print("The following files in the specified directory may have secrets stored in them:\n")

# Run script iterating over each file and directory
for root, dirs, files in os.walk(DIR):
    # Ignore .git directory as this won't hit code control software
    if '.git' in dirs:
        dirs.remove('.git')

    # Open each file and check for secrets
    for file in files:
        single_file = open(root + "/" + file, "r")
        regex = re.compile(r"\b\w{" + re.escape(LENGTH) + r",}\b")

        # Print the data
        for line_number, line in enumerate(single_file, 1):
            data = regex.findall(line)
            for secret in data:
                print("File: " + os.path.join(root, file))
                print("Secret: " + secret)
                print("Line: " + "%d\n" % line_number)
        single_file.close()
