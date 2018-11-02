import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import struct

from SWAPPlaceHolder import *
from .ArtifactSignature import *

class ArtifactTypeChecker:

    def __init__(self):
        pass


    @staticmethod
    def _file_reader(_file_path):
        try:
            _fd = open(_file_path, 'rb')
            _file_bin = _fd.read()
            return _file_bin

        except Exception as e:
            return None


    @staticmethod
    def _is_win_prefetch(_file_bin):
        _win_prefetch_sig = struct.unpack('c'*4, _file_bin[4:8])
        if _win_prefetch_sig == WIN_PREFETCH_SIGNATURE:
            return True
        else:
            return False


    def result(self, _file_path):
        _file_bin = self._file_reader(_file_path)

        if self._is_win_prefetch(_file_bin) is True:
            return WIN_PREFETCH
        else:
            return None


