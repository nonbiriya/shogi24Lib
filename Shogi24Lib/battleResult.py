#勝敗結果を保持するクラス

class battleResult:

    def __init__(self):
        pass

#    #勝敗＋後手のレートの生文字列を格納　→　○●　R1308
#    def setRowString(self,row):
#        self._rowString = row
#    def getRowString(self):
#        return self._rowString

    #棋譜再生ページのURL
    def setPlayAdress(self,playAdress):
        self._PlayAdress = playAdress

    def getPlayAdress(self):
        return self._PlayAdress

    #棋譜ページ
    def setKifuAdress(self,kifuAdress):
        self._kifuAdress = kifuAdress
    def getKifuAdress(self):
        return self._kifuAdress

    #早、15分、30分などのモード
    def setMode(self,mode):
        self._mode = mode
    
    def getMode(self):
        return self._mode

    #対戦日時
    def setDate(self,date):
        self._date = date
    
    def getDate(self):
        return self._date

    #先手レート
    def setFirstMoveRate(self,rate):
        self._firstMoveRate = rate
    
    def getFirstMoveRate(self):
        return self._firstMoveRate

    #先手名前
    def setFirstMoveName(self,name):
        self._firstMoveName = name
    
    def getFirstMoveName(self):
        return self._firstMoveName

    #先手勝敗
    def setFirstMoveWin(self,win):
        self._firstMoveWin = win
    
    def getFirstMoveWin(self):
        return self._firstMoveWin

    #後手レート
    def setLastMoveRate(self,rate):
        self._lastMoveRate = rate
    
    def getLastMoveRate(self):
        return self._lastMoveRate

    #後手名前
    def setLastMoveName(self,name):
        self._lastMoveName = name
    def getLastMoveName(self):
        return self._lastMoveName

    #後手勝敗
    def setLastMoveWin(self,win):
        self._lastMoveWin = win
    def getLastMoveWin(self):
        return self._lastMoveWin

    #手数
    def setNum(self,num):
        self._num = num
    def getNum(self):
        return self._num

    #備考
    def setRemarks(self,remarks):
        self._remarks = remarks
    def getRemarks(self):
        if self._remarks is None:
            return ""
        return self._remarks

    def setKifu(self,kifu):
        self._kifu = kifu
    def getKifu(self):
        return self._kifu
    