#棋譜ファイルを作成するクラス
#https://www.shogidojo.net/kifu/show_kifu.php?id=*******&dd=***************から******.kifを生成して保存
import os
class kifu():

    def __init__(self,BattleResultList):
        self.makeKifu(BattleResultList)

#棋譜ファイルを出力
    def outputKifu(self,filename,kifu):
        os.makedirs("kifu",exist_ok=True)
        print(os.getcwd())
        f = open(filename,'x')
        f.write(kifu)
        f.close()


#棋譜ファイル名を生成
    def makeFileName(self,BattleResult):
        filename = "kifu/"
        filename += BattleResult.getMode()
        filename += "_"
        filename += BattleResult.getDate().replace(' ', '_').replace(':','-')
        filename += "_"
        filename += BattleResult.getFirstMoveName()
        filename += "_"
        filename += BattleResult.getLastMoveName()
        filename += ".kif"
        return filename

#メインクラス
    def makeKifu(self,BattleResultList):
        #棋譜ファイル名生成
        for battleResult in BattleResultList:
            filename = self.makeFileName(battleResult)
        #棋譜出力
            self.outputKifu(filename,battleResult.getKifu())
