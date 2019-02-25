# -*- coding: utf-8 -*-

import configparser

class inifile:
    def __init__(self,filename = None):
        if filename is None:
            self.setIniFile("./setting.ini")
        else:
            self.setIniFile(filename)
        self.readIniFile()

    def setIniFile(self,filename):
        self._inifile = configparser.ConfigParser()
        self._inifile.read(filename, 'UTF-8')
        return self._inifile
    
    def readIniFile(self):
        try:
            self._uname = self._inifile.get("user","id")
            self._pwd   = self._inifile.get("user","pass")
        except:
            return False
        return True

    def getUserName(self):
        return self._uname

    def getUserPass(self):
        return self._pwd
    
