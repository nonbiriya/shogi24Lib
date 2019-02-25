#棋譜ファイルを作成するクラス
#https://www.shogidojo.net/kifu/show_kifu.php?id=*******&dd=***************から******.kifを生成して保存


class kifu():
#棋譜ファイルを出力
    def outputKifu(self,filename,kifu):
        f = open(filename,'w')
        f.write(kifu)
        f.close()


#棋譜ファイル名を生成
    def makeFileName(self,BattleResult):
        filename = "\kifu\\"
        filename  = getMode()
        filename += "_"
        filename += getDate().replace(' ', '_')
        filename += "_"
        filename += getFirstMoveName()
        filename += "_"
        filename += getLastMoveRate()
        fileneme += ".kif"
        return filename

#メインクラス
    def kifu(self,listOfBattleResult):
        #棋譜ファイル名生成
        for battleResult in listOfBattleResult:
            filename = makeFileName(battleResult)
            print(filename)
        #棋譜出力
            outputKifu(filename,battleResult.getKifu())
