import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(path)

import Shogi24Lib

class testlogin(unittest.TestCase):
    def setUp(self):
        self._loginObj = Shogi24Lib.login()

    def testIniFile(self):
        self.assertIsNotNone(self._loginObj.setUserName("name"))
        self.assertIsNotNone(self._loginObj.setUserPass("pass"))
        self.assertIsNotNone(self._loginObj.doLogin())
        self.assertIsNotNone(self._loginObj.getSession())
        self.assertIsNotNone(self._loginObj.setLoginInfo("name","pass"))


if __name__ == "__main__":
    unittest.main()