"""Import modules"""
import os
import argparse

# Setup arguments
parser = argparse.ArgumentParser(
    description='File Extension searches for all files in a' +
    'path with the specified file extension.')
parser.add_argument(
    '-e',
    '--extension',
    required=True,
    help='The file extension to search a path for.'
)
parser.add_argument(
    '-p',
    '--path',
    required=True,
    help='Where File Extension will search for files with the specified file extension.'
)
args = parser.parse_args()


def main():
    """Search for files with a specific extension in the specified directory"""
    dirs_to_ignore = ['node_modules', 'vendor',
                      '.git', '__pycache__', 'build', 'dist']
    for root, dirs, files in os.walk(args.path, topdown=True):
        dirs[:] = [directory for directory in dirs if directory not in dirs_to_ignore]
        for file in files:
            if file.endswith(args.extension):
                print(os.path.join(root, file))


if __name__ == "__main__":
    main()
