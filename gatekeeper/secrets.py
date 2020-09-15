import re
import os
import argparse


class SecretsCLI():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Secrets searches a path for possible secrets in code.')  # noqa
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            type=str,
            help='Where Secrets will search for the string specified in each file.'  # noqa
        )
        parser.add_argument(
            '-l',
            '--length',
            default=16,
            type=int,
            help='The minimum length of the secrets to search for.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        Secrets.run(
            path=self.path,
            length=self.length,
        )


class Secrets():
    @classmethod
    def run(cls, path, length):
        """Search files for secrets such as passwords, API keys, etc
        """
        print('\n####################\nGATEKEEPER - SECRETS\n####################\n')  # noqa
        print('The following files may have secrets stored in them:\n')
        regex_pattern = re.compile(r'\b\w{' + str(length) + r',}\b')
        dirs_to_ignore = [
            'node_modules',
            'vendor',
            '.git',
            '__pycache__',
            'build',
            'dist'
        ]
        if os.path.exists(os.path.join(path, '.gitignore')):
            gitignore = open(os.path.join(path, '.gitignore'), 'r').read().splitlines()  # noqa
        else:
            gitignore = False

        # Run script iterating over each file and directory
        secrets_files = []
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [directory for directory in dirs if directory not in dirs_to_ignore]  # noqa
            for file in files:
                if gitignore and file in gitignore:
                    continue
                filepath = os.path.join(root, file)

                # Open each file and print the findings
                with open(filepath, 'r', encoding='latin1') as single_file:
                    for line_number, line in enumerate(single_file, 1):
                        data = regex_pattern.findall(line)
                        for secret in data:
                            message = f'File: {filepath}\nSecret: {secret}\nLine: {line_number}\n'  # noqa
                            secrets_files.append(message)
                            print(message)
        return secrets_files


def main():
    SecretsCLI().run()


if __name__ == '__main__':
    main()
