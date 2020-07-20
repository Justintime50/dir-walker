"""Import modules"""
import re
import os
import argparse

# Setup arguments
parser = argparse.ArgumentParser(
    description='Secrets searches a path for possible secrets in code.')
parser.add_argument(
    '-p',
    '--path',
    required=True,
    help='Where Secrets will search for the string specified in each file.'
)
parser.add_argument(
    '-l',
    '--length',
    default=16,
    help='The minimum length of the secrets to search for.'
)
args = parser.parse_args()


def main():
    """Search files for secrets such as passwords, API keys, etc"""
    print("\n##################\nGATEKEEPER - SECRETS\n##################\n")
    print("The following files in the specified args.pathectory may have secrets stored in them:\n")
    regex_pattern = re.compile(r"\b\w{" + re.escape(args.length) + r",}\b")
    dirs_to_ignore = ['node_modules', 'vendor',
                      '.git', '__pycache__', 'build', 'dist']
    gitignore = open(os.path.join(args.path, '.gitignore'),
                     'r').read().splitlines()

    # Run script iterating over each file and args.pathectory
    for root, dirs, files in os.walk(args.path, topdown=True):
        dirs[:] = [directory for directory in dirs if directory not in dirs_to_ignore]
        for file in files:
            if file in gitignore:
                continue
            filepath = os.path.join(root, file)

            # Open each file and print the findings
            with open(filepath, "r") as single_file:
                for line_number, line in enumerate(single_file, 1):
                    data = regex_pattern.findall(line)
                    for secret in data:
                        print("File: " + filepath)
                        print("Secret: " + secret)
                        print("Line: " + "%d\n" % line_number)


if __name__ == "__main__":
    main()
