import argparse
import os

class ArgParseWrapper:

    def __init__(self):
        self._arg_parser = argparse.ArgumentParser(
            description='Super Windows Artifact Parser'
        )
        self._set_arguments()
        self._args = self._arg_parser.parse_args()


    def _set_arguments(self):
        _input_options = self._arg_parser.add_mutually_exclusive_group()
        _input_options.required = True

        _input_options.add_argument(
            '-v', '--volume',
            dest='input_volume',
            action='store',
            type=str,
            default=None,
            help='Volume Letter to want to parse'
        )
        _input_options.add_argument(
            '-f', '--file',
            dest='input_file_path',
            action='store',
            type=str,
            default=None,
            help='Artifact file path to want to parse'
        )
        _input_options.add_argument(
            '-d', '--dir',
            dest='input_dir_path',
            action='store',
            type=str,
            default=None,
            help='Artifact directory path to want to parse'
        )


    def get_file_path(self):
        if hasattr(self._args, 'input_file_path'):
            if self._args.input_file_path is not None:
                if os.path.isfile(self._args.input_file_path):
                    return self._args.input_file_path
        return None


    def get_dir_path(self):
        if hasattr(self._args, 'input_dir_path'):
            if self._args.input_dir_path is not None:
                if os.path.isdir(self._args.input_dir_path):
                    return self._args.input_dir_path
        return None