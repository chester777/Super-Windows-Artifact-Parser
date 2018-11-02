import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import struct

from SWAPPlaceHolder import *

WIN_PREFETCH_VERSION_XP_2003 = '0x11'
WIN_PREFETCH_VERSION_VISTA_7 = '0x17'
WIN_PREFETCH_VERSION_8_1 = '0x1a'
WIN_PREFETCH_VERSION_10 = '0x1e'

class WinPrefetchParser:

    def __init__(self):
        self.result = {
            "version": ""
        }


    def result(self, _file_path):
        _fd = open(_file_path, 'rb')
        _version = hex(struct.unpack('i', _fd.read(4))[0])

        # version check
        if _version == WIN_PREFETCH_VERSION_XP_2003:
            self.result["version"] = WIN_VERSION_XP
        elif _version == WIN_PREFETCH_VERSION_VISTA_7:
            self.result["version"] = WIN_VERSION_VISTA
        elif _version == WIN_PREFETCH_VERSION_8_1:
            self.result["version"] = WIN_VERSION_8
        elif _version == WIN_PREFETCH_VERSION_10:
            self.result["version"] = WIN_VERSION_10



        # _win_prefetch_sig = struct.unpack('c' * 4, _file_bin[4:8])