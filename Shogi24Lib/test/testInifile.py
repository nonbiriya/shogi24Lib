import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(path)

import Shogi24Lib

class testInifile(unittest.TestCase):
    def setUp(self):
        self._loginObj = Shogi24Lib.inifile()

    def testIniFile(self):
        self.assertIsNotNone(self._loginObj.setIniFile("setting.ini"))
        self.assertEqual(True,self._loginObj.readIniFile())
        self.assertIsNotNone(self._loginObj.getUserName())
        self.assertIsNotNone(self._loginObj.getUserPass())


if __name__ == "__main__":
    unittest.main()
    