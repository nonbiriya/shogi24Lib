import unittest
from . import battleResult as bt

class testBattleResult(unittest.TestCase):
    
    def testDividRowString(self):

        self.assertEqual(False,bt.dividRowString("aaaa"))


if __name__ == "__main__":
    unittest.main()
