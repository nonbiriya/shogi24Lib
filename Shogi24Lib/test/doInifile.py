import sys, os
path = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(path)

import Shogi24Lib

test = Shogi24Lib.inifile("setting.ini")
print(test.readIniFile())
print(test.setIniFile("setting.ini"))