import argparse
import os
import re


class SequentialRenamerCLI():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Sequential Renamer recursively renames files in a directory in a sequential manner and prepends the parent folder name.'
        )
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            help='Where Sequential Renamer will recursively rename files it finds.'
        )
        parser.add_argument(
            '-f',
            '--force',
            required=False,
            action='store_true',
            help='Force changes which take permenant effect.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        SequentialRenamer.run(
            path=self.path,
            force=self.force,
        )


class SequentialRenamer():
    @staticmethod
    def run(path, force=False):
        """Recursively rename files in a sequential manner, prepending the folder name to 
        a seqential number that restarts in each folder

        Example output:
        /Users/jhammond/Downloads/Justin Skydive 2019/IMG_2462_proc_592015324.jpg  ->  justin-skydive-2019-0.jpg
        /Users/jhammond/Downloads/Justin Skydive 2019/IMG_2494_proc_592015326.jpg  ->  justin-skydive-2019-1.jpg
        /Users/jhammond/Downloads/Justin Skydive 2019/IMG_2514_proc_592015327.jpg  ->  justin-skydive-2019-2.jpg
        """
        files_to_ignore = [
            '.ds_store',
        ]
        dirs_to_ignore = [
            'photos library.photoslibrary',
        ]

        print('Sequential Renamer in progress, this could take awhile...')
        files_updated = 0
        for root, dirs, files in os.walk(path, topdown=True):
            files[:] = [filename for filename in files if filename.lower() not in files_to_ignore]
            dirs[:] = [directory for directory in dirs if directory.lower() not in dirs_to_ignore]
            for i, full_filename in enumerate(files):
                filename = os.path.splitext(full_filename)[0].lower()
                file_extension = os.path.splitext(full_filename)[1].lower()

                folder_name = os.path.basename(os.path.dirname(os.path.join(root, full_filename)))
                slugged_folder_name = folder_name.replace('_', '-').replace(' ', '-')

                files_updated += 1
                new_filename = (re.sub(r'[^0-9a-zA-Z-_]+', '', slugged_folder_name) + '-' + str(i) + file_extension).lower()  # noqa

                if force:
                    os.rename(os.path.join(root, full_filename), os.path.join(root, new_filename))
                else:
                    print(os.path.join(root, full_filename) + '  ->  ' + new_filename)

        if force:
            print(f'Process complete, {files_updated} records were updated!')
        else:
            print(f'{files_updated} records will be updated when forced.')
            print('DRY RUN complete, run with the "--force" flag to actually rename files.')


def main():
    SequentialRenamerCLI().run()


if __name__ == '__main__':
    main()
