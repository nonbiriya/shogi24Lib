#棋譜一覧ページをスクレイピングして対戦結果を取得するクラス
#https://www.shogidojo.net/kifu/?duid=*****&all=onから取得
from . import battleResult
from bs4 import BeautifulSoup

class kifuListPage():
    _search_baseurl = "https://www.shogidojo.net/kifu/?duid="
    _link_baseurl = "https://www.shogidojo.net"

	#コンストラクタ。
    #スクレイピングを行うのでセッション必須
    def __init__(self,session):
        self._session = session
    
    #２４ID
    def setId(self,id):
        self._id = id
    
    def getId(self):
        return self._id
    
    #セッションからHTMLを取得してBSに渡す。
    def getListPage(self):
        self._postUrl = self._search_baseurl + self._id
        self._kifuPage = self._session.post(self._postUrl)
        self._soup = BeautifulSoup(self._kifuPage.content, "html.parser")
        return self._soup
    
    def getListPageAll(self):
        self._postUrl = self._search_baseurl + self._id + "&all=on"
        self._kifuPage = self._session.post(self._postUrl)
        self._soup = BeautifulSoup(self._kifuPage.content, "html.parser")
        return self._soup
    
    def getKifu(self,kifuUrl):
        kifuget = self._session.post(kifuUrl)
        self._kifusoup = BeautifulSoup(kifuget.content,"html.parser",from_encoding="SJIS")
        return self._kifusoup

    #スクレイピング実行
    def scrapingListPage(self):
        #棋譜一覧のtableタグを探す
        kiftable = self._soup.find("table",id="topKifu_table")
        #trタグが１局
        #<tr style="height:34px;">
        #<td>
            #<a class="downloadkifufile" download="45048126_0209_[yawatashell]1325_ox_[nonbiriya]1348.kif" href="/kifu/show_kifu.php?id=45048126&amp;dd=1afaed24d40a1e2d195cb8b12a83505e" style="display:none">45048126_0209_[yawatashell]1325_ox_[nonbiriya]1348</a>
            #<a class="topKifu_group" href="/kifu/kifudisplay.php?kifuid=45048126&amp;dd=1afaed24d40a1e2d195cb8b12a83505e">
                #<img src="/images/top/kifu_btn.png"/>
            #</a>
        #</td>
        #<td>R早2</td>
        #<td>2/9 13:41</td>
        #<td>R1325
            #<form action="/player/" id="kifu_form0" method="POST" name="kifu_form0" style="display:inline;">
            #<a href="javascript:document.forms['kifu_form0'].submit()">
            #<span class="fc03">yawatashell</span>
            #</a>
            #<input name="userid" type="hidden" value="73747"/>
            #　○●　R1348　<span>nonbiriya</span>
            #</form>　
            #157手
        #</td>
        #</tr>
        battles = kiftable.find_all("tr")
        self._resultList = []
        for battle in battles:
            if "東京棋譜はありません" in battle.text:
                continue
            bufBattleResult = battleResult()
            #棋譜URL
            bufBattleResult.setKifuAdress(self._link_baseurl + battle.find("a",class_="downloadkifufile").get("href"))
            #棋譜
            bufBattleResult.setPlayAdress(self._link_baseurl + battle.find("a",class_="topKifu_group").get("href"))
            kifu = self.getKifu(bufBattleResult.getKifuAdress())
            bufBattleResult.setKifu(kifu.text)

            textes = battle.find_all("td")
            #早指しなどの区分
            bufBattleResult.setMode(textes[1].text)
            #対局開始日時
            bufBattleResult.setDate(textes[2].text)
            
            #先手R、先手name,先手勝敗、後手勝敗、後手name,後手R、手数
            trimText = textes[3].text.replace('\n','')
            buftext = trimText.split('　')
            #先手R
            bufBattleResult.setFirstMoveRate(buftext[0])
            #先手name
            bufBattleResult.setFirstMoveName(buftext[1])
            #後手R
            bufBattleResult.setLastMoveRate(buftext[3])
            #後手name
            bufBattleResult.setLastMoveName(buftext[4])
            #手数
            bufBattleResult.setNum(buftext[5])
            #備考
            if len(buftext) > 6:
                bufBattleResult.setRemarks(buftext[6])
            else:
                bufBattleResult.setRemarks("")
            #勝敗
            if buftext[2] == "○●":
                bufBattleResult.setFirstMoveWin(True)
                bufBattleResult.setLastMoveWin(False)
            else:
                bufBattleResult.setFirstMoveWin(False)
                bufBattleResult.setLastMoveWin(True)
            
            self._resultList.append(bufBattleResult)
        
        return self._resultList

    def getResultList(self):
        return self._resultList

