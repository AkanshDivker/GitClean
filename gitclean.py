'''This module is the main module of the program and handles its input and entry point.'''

import argparse
import glob
import os
import sys
from loguru import logger


class GitClean:
    '''Class to receive and process input for GitClean and then execute main components.'''

    @staticmethod
    def run():
        '''Main entry point for GitClean.'''

        parser = argparse.ArgumentParser()

        parser.add_argument(
            '-c',
            '--clean',
            help='Cleans the specified directory with the selected options.',
            action='store')

        parser.add_argument('-e',
                            '--extensions',
                            nargs='+',
                            type=str,
                            required=True,
                            help='Extension of files to filter for cleaning.')

        parser.add_argument(
            '-r',
            '--remove',
            help='''To specify whether to remove the filtered files.
             Otherwise, filtered files will be kept and all others will be removed.''',
            action='store_true')

        args = parser.parse_args()

        GitClean.setup_logger()

        if args.clean:
            files = GitClean.clean(args.clean, tuple(args.extensions),
                                   args.remove)
            logger.success(f'GitClean successfully removed {files} files.')

    @staticmethod
    def clean(directory: str, extensions: tuple, remove: bool) -> int:
        '''Function to filter through files and remove them.'''
        files = 0

        for file in glob.iglob(directory + '/**', recursive=True):
            if remove:
                if os.path.isfile(file) and file.endswith(extensions):
                    try:
                        logger.info(f'Removing file {file}')
                        os.remove(file)
                        files += 1
                    except OSError:
                        logger.error(f'''Encountered OS Error while removing
                             file {file} from directory.''')
            else:
                if os.path.isfile(file) and file.endswith(extensions):
                    continue

                if not os.path.isdir(file):
                    try:
                        logger.info(f'Removing file {file}')
                        os.remove(file)
                        files += 1
                    except OSError:
                        logger.error(f'''Encountered OS Error while removing
                             file {file} from directory.''')

        return files

    @staticmethod
    def setup_logger():
        '''Setup and configure the loguru logger.'''
        logger.remove()

        logger.add(
            sys.stdout,
            colorize=True,
            format=
            "<cyan>{time}</cyan> | <level>{level}</level> | <level>{message}</level>"
        )


if __name__ == '__main__':
    GitClean.run()
