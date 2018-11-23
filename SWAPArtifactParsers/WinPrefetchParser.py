import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import struct
from datetime import datetime, timedelta

from SWAPPlaceHolder import *
from SWAPUtils.DateFormatter import *

WIN_PREFETCH_VERSION_XP_2003 = '0x11'
WIN_PREFETCH_VERSION_VISTA_7 = '0x17'
WIN_PREFETCH_VERSION_8_1 = '0x1a'
WIN_PREFETCH_VERSION_10 = '0x1e'

class WinPrefetchParser:

    def __init__(self):
        self._win_prefetch_info = {
            'version': '',
            'signature': '',
            'size': '',
            'origin_filename': '',
            'hash': '',
            'execute_count': '',
            'latest_execute_time': '',
            'handling_file_list': ''
        }


    @staticmethod
    def _get_time(big):
        little = ''
        for i in range(0, len(big), 2):
            little += big[-(i + 2)]
            little += big[-(i + 1)]
        return str(datetime(1601, 1, 1) + timedelta(microseconds=(int(little, 16) / 10), hours=+9))


    def _parse_by_win_xp(self):
        self._win_prefetch_info['execute_count'] = struct.unpack('<L', self._file_bin[0x90:0x90 + 4])[0]
        self._win_prefetch_info['latest_execute_time'] = self._get_time(self._file_bin[0x78:0x78 + 8].hex())


    def _parse_by_win_7(self):
        self._win_prefetch_info['execute_count'] = struct.unpack('<L', self._file_bin[0x98:0x98 + 4])[0]
        self._win_prefetch_info['latest_execute_time'] = self._get_time(self._file_bin[0x80:0x80 + 8].hex())


    def _parse_by_win_8_1(self):
        self._win_prefetch_info['execute_count'] = struct.unpack('<L', self._file_bin[0x98:0x98 + 4])[0]
        self._win_prefetch_info['latest_execute_time'] = self._get_time(self._file_bin[0x80:0x80 + 8].hex())


    def _parse_by_win_10(self):
        self._win_prefetch_info['execute_count'] = struct.unpack('<L', self._file_bin[0xD0:0xD0 + 4])[0]
        self._win_prefetch_info['latest_execute_time'] = self._get_time(self._file_bin[0x80:0x80 + 8].hex())


    def result(self, _file_path):
        _fd = open(_file_path, 'rb')
        self._file_bin = _fd.read()

        # file header check - compressed prefetch
        _file_header = '0x' + '0x'.join(list(a.hex() for a in struct.unpack('4c', self._file_bin[0x4:0x4 + 4])))


        # get prefetch version
        _version = hex(struct.unpack('i', self._file_bin[0x0:0x0+4])[0])

        if _version == WIN_PREFETCH_VERSION_XP_2003:
            self._win_prefetch_info['version'] = WIN_VERSION_XP
        elif _version == WIN_PREFETCH_VERSION_VISTA_7:
            self._win_prefetch_info['version'] = WIN_VERSION_7
        elif _version == WIN_PREFETCH_VERSION_8_1:
            self._win_prefetch_info['version'] = WIN_VERSION_8
        elif _version == WIN_PREFETCH_VERSION_10:
            self._win_prefetch_info['version'] = WIN_VERSION_10

        # get prefetch signature
        _win_prefetch_sig = '0x' + '0x'.join(list(a.hex() for a in struct.unpack('4c', self._file_bin[0x4:0x4+4])))
        self._win_prefetch_info['signature'] = _win_prefetch_sig

        # get prefetch size
        _prefetch_size = struct.unpack('i', self._file_bin[0xc:0xc+4])[0]
        self._win_prefetch_info['size'] = _prefetch_size

        # get original file name
        _origin_file_name = struct.unpack('60s', self._file_bin[0x10:0x10+60])[0]\
                                  .split(b'\x00\x00')[0]\
                                  .replace(b'\x00', b'').decode('utf-8')
        self._win_prefetch_info['origin_filename'] = _origin_file_name

        # get prefetch hash
        _prefetch_hash = hex(struct.unpack('<L', self._file_bin[0x4c:0x4c+4])[0])
        self._win_prefetch_info['hash'] = _prefetch_hash


        if self._win_prefetch_info['version'] == WIN_VERSION_XP:
            self._parse_by_win_xp()

        elif self._win_prefetch_info['version'] == WIN_VERSION_7:
            self._parse_by_win_7()

        elif self._win_prefetch_info['version'] == WIN_VERSION_8:
            self._parse_by_win_8_1()

        elif self._win_prefetch_info['version'] == WIN_VERSION_10:
            self._parse_by_win_10()

        return self._win_prefetch_info