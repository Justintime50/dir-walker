<div align="center">

# Gatekeeper

Gatekeeper is a suite of tools that sees and knows all about your code.

[![Build Status](https://travis-ci.com/Justintime50/gatekeeper.svg?branch=master)](https://travis-ci.com/Justintime50/gatekeeper)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/gatekeeper/badge.svg?branch=master)](https://coveralls.io/github/Justintime50/gatekeeper?branch=master)
[![PyPi](https://img.shields.io/pypi/v/gatekeeper-suite)](https://pypi.org/project/gatekeeper-suite/)
[![Licence](https://img.shields.io/github/license/justintime50/gatekeeper)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

Gatekeeper is the perfect companion to any source control workflow. Find files still containing secrets or search for specific file types or strings of characters you may have forgotten to add to your gitignore. Gatekeeper will keep your git history safe and your development a bit less stressful. Longterm, Gatekeeper is intended to be a completely automated suite of tools that can be used to keep code safe, git history clean, and correct silly human error.

## Install

```bash
# Install tool
pip3 install gatekeeper-suite

# Install locally
make install

# Get Makefile help
make help
```

## Usage

### Gatekeeper File Extension

File Extension searches for all files in a path with the specified file extension.

```
Usage:
    gatekeeper-file-extension --path ~/code/my_project --extension ".py"

Options:
    -h, --help                              show this help message and exit
    -p PATH, --path PATH                    Where File Extension will search for files with the specified file extension.
    -e EXTENSION, --extension EXTENSION     The file extension to search a path for.
```

### Gatekeepeer Scout

Scout searches through a directory for any string of text you specify. Perfect for searching across multiple projects or large code bases.

```
Usage:
    gatekeeper-scout --path ~/code/my_project --search "My string of text"

Options:
    -h, --help                  show this help message and exit
    -p PATH, --path PATH        Where Scout will search for the string specified in each file.
    -s SEARCH, --search SEARCH  The string to search for in each file of a path.
```

### Gatekeeper Secrets

Secrets searches a path for possible secrets in code. Perfect for finding any passwords, API keys, or secrets you were about to commit.

```
Usage:
    gatekeeper-secrets --path ~/code/my_project --length 20

Options:
    -h, --help                    show this help message and exit
    -p PATH, --path PATH          Where Secrets will search for the string specified in each file.
    -l LENGTH, --length LENGTH    The minimum length of the secrets to search for.
```

### Gatekeeper Sequential Renamer

Sequential Renamer recursively renames files in a directory in a sequential manner and prepends the parent folder name.

```
Usage:
    gatekeeper-sequential-renamer --path ~/path/to/photos --force

Options:
    -h, --help            show this help message and exit
    -p PATH, --path PATH  Where Sequential Renamer will recursively rename files it finds.
    -f, --force           Force changes which take permenant effect.
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run the scripts locally
venv/bin/python gatekeeper/secrets.py --help
```

## Attribution

* Icons on README made by <a href="https://www.flaticon.com/free-icon/castle_3125375" title="Icongeek26">Icongeek26</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
