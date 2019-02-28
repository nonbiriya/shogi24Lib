from bs4 import BeautifulSoup
from . import memberSearchResult
import json

#https://web.shogidojo.net/24member/meibo/　をスクレイピングしてユーザIDを検索する

class searchUser():
    _memberSearchResultList = []
    _searchUrl = "https://web.shogidojo.net/24member/meibo/"

    def __init__(self,session,userName):
        self._session = session
        self._userName = userName

#検索結果をクラスに格納する
    def search(self):
        searchResult = self.getSearchResult()
        soup = BeautifulSoup(searchResult.content, "html.parser")
        searchResultTable = self.findTableTag(soup)
        members = self.findTrTags(searchResultTable)
        return self.getMembers(members)


    def getSearchResult(self):
        payload = {'nameHead': self._userName,'strength':'0','games':'0','localityHead':'','sub':'検索'}
        return self._session.post(self._searchUrl, data=payload)

    def findTableTag(self,soup):
        return soup.find("table",id="myTable")

    def findTrTags(self,searchResultTable):
        return searchResultTable.find_all("tr")
    
    def getMembers(self,members):
        for member in members:
            result = memberSearchResult.memberSearchResult()
            data = member.find_all("td")
            if len(data)==0:
                continue
			#ユーザ名
            result.setUserName(data[1].text)
            result.setDankyu(data[2].text)
            result.setR(data[3].text)
            result.setWinRate(data[4].text) 
            result.setWin(data[5].text) 
            result.setLose(data[6].text) 
            result.setDrow(data[7].text)
            result.setBattle(data[8].text) 
            result.setMaxR(data[9].text) 
            result.setResion(data[10].text)
            result.setProf(data[11].text) 
            result.setUserId(data[12].text)
            self._memberSearchResultList.append(result)
        return self._memberSearchResultList


    def getMemberSearchResultList(self):
        return self._memberSearchResultList

#検索結果格納クラスから一致した結果を返す
    def match(self):
        if self._memberSearchResultList is None:
            return None
        for member in self._memberSearchResultList:
            if member.getUserName() == self._userName:
                return member
        return None
        
    def getMatchId(self):
        member = self.match()
        if member is not None:
            return member.getUserId()


