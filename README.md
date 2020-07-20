<div align="center">

# Gatekeeper

Gatekeeper is a suite of tools that sees and knows all about your code.

[![Build Status](https://travis-ci.com/Justintime50/gatekeeper.svg?branch=master)](https://travis-ci.com/Justintime50/gatekeeper)
[![Pypi](https://img.shields.io/pypi/v/gatekeeper-suite)](https://pypi.org/project/gatekeeper-suite/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

Gatekeeper is the perfect companion to any source control workflow. Find files still containing secrets or search for specific file types or strings of characters you may have forgotten to add to your gitignore. Gatekeeper will keep your git history safe and your development a bit less stressful. Longterm, Gatekeeper is intended to be a completely automated suite of tools that can be used to keep code safe, git history clean, and correct silly human error.

## Install

```bash
pip3 install gatekeeper-suite
```

## Usage

### Gatekeeper File Extension

File Extension searches for all files in a path with the specified file extension.

```
Usage:
    gatekeeper-file-extension --extension ".py" --path ~/code/my_project

Options:
    -h, --help                              show this help message and exit
    -e EXTENSION, --extension EXTENSION     The file extension to search a path for.
    -p PATH, --path PATH                    Where File Extension will search for files with the specified file extension.
```

### Gatekeepeer Scout

Scout searches through a directory for any string of text you specify. Perfect for searching across multiple projects or large code bases.

```
Usage:
    gatekeeper-scout --search "My string of text" --path ~/code/my_project

Options:
    -h, --help                  show this help message and exit
    -s SEARCH, --search SEARCH  The string to search for in each file of a path.
    -p PATH, --path PATH        Where Scout will search for the string specified in each file.
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

## Development

```bash
# Install pylint
pip3 install -e ."[dev]"

# Lint files
pylint gatekeeper/*.py
```

## Attribution

* Icons on README made by <a href="https://www.flaticon.com/free-icon/castle_3125375" title="Icongeek26">Icongeek26</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
