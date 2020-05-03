# Gatekeeper

Suite of tools to keep code safe, keep git history clean, and correct silly human error.

[![Build Status](https://travis-ci.com/Justintime50/gatekeeper.svg?branch=master)](https://travis-ci.com/Justintime50/gatekeeper)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

Gatekeeper is the perfect companion to any source control workflow. Find files still containing secrets or search for specific file types you may have forgotten to add to your gitignore. Gatekeeper will keep your git history safe and your life a bit more stress free. Longterm, Gatekeeper is intended to be a completely automated suite of tools that can be used to keep code safe, git history clean, and correct silly human error.

## Usage

Currently, Gatekeeper is a manual tool that must be run via the command line.

### Gatekeeper File Extension Search

Search for files with whatever file extension and in whatever directory you provide and return what it finds.

```bash
python3 gatekeeper_file_ext.py
```

### Gatekeeper Secrets Search

Search a directory you specify for alphanumeric strings in every file in the directory. Perfect for finding any passwords, API keys, or secrets you were about to commit.

You should specify the root directory of the project you want Gatekeeper to check.

```bash
python3 gatekeeper_secrets.py /path/to/my/project/dir
```

## Development

```bash
# Install pylint
pip3 install pylint

# Lint files
pylint src/*.py
```
