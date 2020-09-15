# CHANGELOG

## v1.1.0 (2020-09-15)

* Added unit tests and test coverage
* Scripts now properly return values
* Updated documentation
* Added a Makefile
* Gatekeeper Scout now prints the entire line your search query is found on instead of simply the search query (closes #4)
* Fixed a bug that could not properly open files based on encoding (closes #5)
* Additional code refactors to place everything into proper classes and functions
* Automated releasing via Travis

## v1.0.0 (2020-07-19)

* Published to PyPi and added setup.py
* Switched to argparse
* Cleaned up each script and documentation
* Added a new script that can search a directory for any string of text

## v0.2.0 (2020)

* Added a secrets search script that can search a directory for potential secrets that remain in code

## v0.1.0 (2020)

* Initial release
* Ability to search a directory for a set of files with the same file extension
