# -*- coding: utf-8 -*-

import configparser


class inifile:

    def __init__(self):
        inifile = configparser.ConfigParser()
        inifile.read('./Shogi24Lib/setting.ini', 'UTF-8')
        self._uname = inifile.get("user","id")
        self._pwd = inifile.get("user","pass")

    def getUserName(self):
        return self._uname

    def getUserPass(self):
        return self._pwd
    
