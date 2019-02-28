import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(path)

import Shogi24Lib


class testBattleResult(unittest.TestCase):
    def setUp(self):
        self._testLogin = Shogi24Lib.login()
        self._searchUser = Shogi24Lib.searchUser(self._testLogin.doLogin(),"nonbiriya")
        self._searchUser.search()
        
    def testGetMemberSearchResultList(self):
        memberlist = self._searchUser.getMemberSearchResultList()
        self.assertIsNotNone(memberlist)
        member = self._searchUser.match()
        self.assertIsNotNone(member)
        self.assertEqual("147126",self._searchUser.getMatchId())
        self.assertEqual("nonbiriya",member.getUserName())
        self.assertEqual("147126",member.getUserId())
        self.assertIsNotNone(member.getDanKyu())
        self.assertIsNotNone(member.getR())
        self.assertIsNotNone(member.getWinRate())
        self.assertIsNotNone(member.getWin())
        self.assertIsNotNone(member.getLose())
        self.assertIsNotNone(member.getDrow())
        self.assertIsNotNone(member.getBattle())
        self.assertIsNotNone(member.getMaxR())
        self.assertEqual("shinshu",member.getResion())
        self.assertEqual("ただの将棋好きです",member.getProf())

if __name__ == "__main__":
    unittest.main()
    