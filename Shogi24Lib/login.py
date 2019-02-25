#ログインしセッションを保持するクラス
from . import inifile
import requests,json

class login:

    def __init__(self,id = None,password = None):
        #iniファイル読み込み
        self._loginInfo = inifile()
        #ログイン情報設定
        self.setLoginInfo(id,password)

    
    def setUserName(self,id):
        if id is None:
            self._userName = self._loginInfo.getUserName()
        else:
            self._userName = id
        return self._userName
    
    def setUserPass(self,password):
        if password is None:
            self._userPass = self._loginInfo.getUserPass()
        else:
            self._userPass = password
        return self._userPass

    def getSession(self):
        return self._session

    def doLogin(self):
        url_login = "https://www.shogidojo.net/login/"
        self._session = requests.session()
        #ログイン
        self._session.post(url_login,data=self._login_info)
        return self._session

    def setLoginInfo(self,id,password):
        self.setUserName(id)
        self.setUserPass(password)
        
        self._login_info = {
            "uname":self._userName,
            "pwd":self._userPass
        }
        return True



