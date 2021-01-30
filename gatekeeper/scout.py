import argparse
import os
import re


class ScoutCLI():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Scout searches through a directory for any string of text you specify.'
        )
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            help='Where Scout will search for the string specified in each file.'
        )
        parser.add_argument(
            '-s',
            '--search',
            required=True,
            help='The string to search for in each file of a path.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        Scout.run(
            path=self.path,
            search=self.search,
        )


class Scout():
    @classmethod
    def run(cls, path, search):
        """Run script iterating over each file and directory
        """
        print('\n##################\nGATEKEEPER - SCOUT\n##################\n')
        print('Gatekeeper Scout found the following for your search query:\n')
        dirs_to_ignore = [
            'node_modules',
            'vendor',
            '.git',
            '__pycache__',
            'build',
            'dist'
        ]
        regex_pattern = re.compile(search)

        # Scout for the search query in all subdirectories of the one specified
        scout_files = []
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [directory for directory in dirs if directory not in dirs_to_ignore]
            for file in files:
                filepath = os.path.join(root, file)

                # Open each file and print the findings
                with open(filepath, 'r') as single_file:
                    for line_number, line in enumerate(single_file, 1):
                        data = regex_pattern.findall(line)
                        for search in data:
                            message = f'File: {filepath}\nSearch: {line.strip()}\nLine: {line_number}\n'
                            scout_files.append(message)
                            print(message)
        return scout_files


def main():
    ScoutCLI().run()


if __name__ == '__main__':
    main()
