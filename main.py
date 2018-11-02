import os

from SWAPPlaceHolder import *
from SWAPUtils.ArgParseWrapper import *
from SWAPUtils.ArtifactTypeChecker import *
from SWAPArtifactParsers.WinPrefetchParser import *

class Main:

    def __init__(self):
        self.__args = ArgParseWrapper()
        self.__type_checker = ArtifactTypeChecker()

        if self.__args.get_dir_path() is not None and self.__args.get_file_path() is None:
            # directory input mode
            for _path, _dir, _files in os.walk(self.__args.get_dir_path()):
                for _file in _files:
                    _file_full_path = os.path.join(_path, _file)
                    _artifact_type = self.__type_checker.result(_file_full_path)

                    _result = None
                    if _artifact_type is WIN_PREFETCH:
                        _parser = WinPrefetchParser()
                        _result = _parser.result(_file_full_path)

        elif self.__args.get_file_path()is not None and self.__args.get_dir_path() is None:
            # file input mode
            _artifact_type = self.__type_checker.result(self.__args.get_file_path())
            _result = None
            if _artifact_type is WIN_PREFETCH:
                _parser = WinPrefetchParser()
                _result = _parser.result(self.__args.get_file_path())

if __name__ == "__main__":
    Main()