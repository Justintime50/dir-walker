<div align="center">

# Rover IO

Rover IO is a suite of tools traverses your directories and performs IO file operations.

[![Build Status](https://github.com/Justintime50/roverio/workflows/build/badge.svg)](https://github.com/Justintime50/withbond-easpost/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/roverio/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/roverio?branch=master)
[![PyPi](https://img.shields.io/pypi/v/roverio)](https://pypi.org/project/roverio/)
[![Licence](https://img.shields.io/github/license/justintime50/roverio)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

Rover IO is the perfect companion to any source control workflow. Find files still containing secrets or search for specific file types or strings of characters you may have forgotten to add to your gitignore. Rename massive collections of files sequentially and recursively (perfect for something like a photo library).

## Install

```bash
# Install tool
pip3 install roverio

# Install locally
make install

# Get Makefile help
make help
```

## Usage

### File Extension

File Extension searches for all files in a path with the specified file extension and returns all the specified results.

```
Usage:
    roverio-file-extension --path ~/code/my_project --extension ".py"

Options:
    -h, --help                              show this help message and exit
    -p PATH, --path PATH                    Where File Extension will search for files with the specified file extension.
    -e EXTENSION, --extension EXTENSION     The file extension to search a path for.
```

### Scout

Scout searches through a directory for any string of text you specify. Perfect for searching across multiple projects or large code bases.

```
Usage:
    roverio-scout --path ~/code/my_project --search "My string of text"

Options:
    -h, --help                  show this help message and exit
    -p PATH, --path PATH        Where Scout will search for the string specified in each file.
    -s SEARCH, --search SEARCH  The string to search for in each file of a path.
```

### Secrets

Secrets searches a path for possible secrets in code. Perfect for finding any passwords, API keys, or secrets you were about to commit. This is accomplished through loose searching of strings of a certain length and is not foolproof in determining what an actual secret is vs a long string.

```
Usage:
    roverio-secrets --path ~/code/my_project --length 20

Options:
    -h, --help                    show this help message and exit
    -p PATH, --path PATH          Where Secrets will search for the string specified in each file.
    -l LENGTH, --length LENGTH    The minimum length of the secrets to search for.
```

### Sequential Renamer

Sequential Renamer recursively renames files in a directory in a sequential manner and prepends the parent folder name. The filename is slugified and lowercased for a uniform naming scheme.

A perfect use case for Seqential Renamer is a large photo library where filenames may be all over the place such as `IMG_1234.JPG` and you want them renamed according to folder. This script has been tested with a library of `10,000` photos.

```
Usage:
    roverio-sequential-renamer --path ~/path/to/photos --force

Options:
    -h, --help            show this help message and exit
    -p PATH, --path PATH  Where Sequential Renamer will recursively rename files it finds.
    -f, --force           Force changes which take permenant effect.
```

**Sample Output**

```
/Users/jhammond/Downloads/Justin's Skydive 2019/IMG_2462_proc_592015324.JPG  ->  justins-skydive-2019-0.jpg
/Users/jhammond/Downloads/Justin's Skydive 2019/IMG_2494_proc_592015326.JPG  ->  justins-skydive-2019-1.jpg
/Users/jhammond/Downloads/Justin's Skydive 2019/IMG_2514_proc_592015327.JPG  ->  justins-skydive-2019-2.jpg
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage

# Run the scripts locally
venv/bin/python roverio/secrets.py --help
```

## Attribution

* Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
