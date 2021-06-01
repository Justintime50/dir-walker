import argparse
import csv
import os
import re

from pretty_tables import PrettyTables

from roverio.constants import DIRS_TO_IGNORE

README_STRING = os.getenv('README_STRING', 'readme.md')


class Cli():
    def __init__(self):
        parser = argparse.ArgumentParser(description='Reads the contents of README files.')
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            help='The path where the tool will search for README\'s.'
        )
        parser.add_argument(
            '-r',
            '--rules',
            required=True,
            help='The path to your rule text file.'
        )
        parser.add_argument(
            '-l',
            '--lazy',
            required=False,
            default=False,
            action='store_true',
            help='Match rules lazily (case-insensitive).'
        )
        parser.add_argument(
            '-c',
            '--create_csv',
            required=False,
            default=False,
            action='store_true',
            help='Save output to a CSV file.'
        )
        parser.add_argument(
            '--csv_path',
            required=False,
            default='readmy_readmes.csv',
            help='The file path where a CSV file will be saved. By default, it will be saved to the current directory.'  # noqa
        )
        parser.parse_args(namespace=self)

    def run(self):
        ReadmyReadmes.run_cli(
            path=self.path,
            rules=self.rules,
            lazy=self.lazy,
            create_csv=self.create_csv,
            csv_path=self.csv_path,
        )


class ReadmyReadmes():
    @staticmethod
    def run_cli(path, rules, create_csv=False, csv_path='readmy_readmes.csv', lazy=False):
        """Run this tool via CLI and print to console
        """
        readmes = ReadmyReadmes.iterate_readmes(path, rules, create_csv, csv_path, lazy)
        print(readmes)

    @staticmethod
    def iterate_readmes(path, rules, create_csv=False, csv_path='readmy_readmes.csv', lazy=False):
        """Iterate through README files looking for each rule.
        Build a table of data based on what is found.
        """
        rules = ReadmyReadmes._open_rules_file(rules)

        # Setup headers
        headers = ['README File']
        for rule in rules:
            headers.append(rule)

        # Setup rows
        rows = []
        readmes = ReadmyReadmes.find_readmes(path)
        for readme in readmes:
            readme_regex = re.compile(fr'{path}/(?P<readme>.+)')
            readme_path_short = readme_regex.search(readme)
            row = [readme_path_short['readme']]
            readme_contents = ReadmyReadmes._open_readme_file(readme)
            for rule in rules:
                row.append(ReadmyReadmes._check_rules_in_readme(readme_contents, rule, lazy))
            rows.append(row)
        sorted_rows = sorted(rows)

        # Setup Pretty Table
        table = PrettyTables.generate_table(
            headers=headers,
            rows=sorted_rows,
        )

        # Setup CSV (if elected)
        if create_csv:
            ReadmyReadmes._create_csv(headers, sorted_rows, csv_path)

        return table

    @staticmethod
    def _open_rules_file(rules):
        """Reads the contents of the rules file
        """
        with open(rules, 'r') as rule_file:
            rules = rule_file.read().split('\n')
        rules.remove('')  # Remove any blank items due to empty lines
        return rules

    @staticmethod
    def _open_readme_file(readme):
        """Reads the contents of a README file
        """
        with open(readme, 'r') as readme_file:
            readme_contents = readme_file.read()
        return readme_contents

    @staticmethod
    def _create_csv(headers, data, csv_path):
        """Create a CSV file
        """
        try:
            data.insert(0, headers)
            with open(csv_path, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
        except Exception as error:
            raise Exception(error)

    @staticmethod
    def find_readmes(path):
        """Walks a folder structure looking for README files and
        returns a list of the paths of each README found.
        """
        readme_list = []
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [directory for directory in dirs if directory not in DIRS_TO_IGNORE]
            for filename in files:
                if README_STRING.lower() in filename.lower():
                    readme_path = f'{root}/{filename}'
                    readme_list.append(readme_path)

        if readme_list == []:
            raise FileNotFoundError('No README files were found with the specified path.')

        return readme_list

    @staticmethod
    def _check_rules_in_readme(readme, rule, lazy=False):
        """Checks if a rule exists in a README file and returns a boolean
        if the rule is found within the README file.
        """
        if lazy:
            if rule.lower() in readme.lower():
                return True
        if not lazy:
            if rule in readme:
                return True
        return False


def main():
    Cli().run()


if __name__ == '__main__':
    main()
