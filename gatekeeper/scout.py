"""Import modules"""
import re
import os
import argparse

# Setup arguments
parser = argparse.ArgumentParser(
    description='Scout searches through a directory for any string of text you specify.')
parser.add_argument(
    '-s',
    '--search',
    required=True,
    help='The string to search for in each file of a path.'
)
parser.add_argument(
    '-p',
    '--path',
    required=True,
    help='Where Scout will search for the string specified in each file.'
)
args = parser.parse_args()


def main():
    """Run script iterating over each file and directory"""
    print("\n##################\nGATEKEEPER - SCOUT\n##################\n")
    print("Gatekeeper Scout found the following for your search query:\n")
    dirs_to_ignore = ['node_modules', 'vendor',
                      '.git', '__pycache__', 'build', 'dist']
    regex_pattern = re.compile(args.search)

    # Scout for the search query in all subdirectories of the one specified
    for root, dirs, files in os.walk(args.path, topdown=True):
        dirs[:] = [directory for directory in dirs if directory not in dirs_to_ignore]
        for file in files:
            filepath = os.path.join(root, file)

            # Open each file and print the findings
            with open(filepath, "r") as single_file:
                for line_number, line in enumerate(single_file, 1):
                    data = regex_pattern.findall(line)
                    for search in data:
                        print("File: " + filepath)
                        print("Search: " + search)
                        print("Line: " + "%d\n" % line_number)


if __name__ == "__main__":
    main()
