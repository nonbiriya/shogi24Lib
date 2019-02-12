#ログインしセッションを保持するクラス
from . import inifile
import requests,json

class login():

    def __init__(self):
        url_login = "https://www.shogidojo.net/login/"
        loginInfo = inifile()
        self._userName = loginInfo.getUserName()
        self._userPass = loginInfo.getUserPass()
        self._login_info = {
            "uname":self._userName,
            "pwd":self._userPass
        }
        self._session = requests.session()

        #ログイン
        self._session.post(url_login,data=self._login_info)

    def getSession(self):
        return self._session