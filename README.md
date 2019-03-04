# shogi24Lib
将棋倶楽部２４から、棋譜、対局結果をスクレイピングするライブラリです。
BSD Licenseに準拠しています。

# 使用例

本ライブラリをプロジェクト下に配置してお使いください
提供しているクラスは以下です

クラス
・inifile
・login
・kifuListPage
・searchUser


# inifile

iniファイルを読み込むクラスです。
setting.iniに将棋倶楽部２４のユーザ名とパスワードを設定してください。

設定例

----------------------------
[user]
id=nonbiriya
pass=password

----------------------------

setting.iniを設定した上で
inifile()で設定ファイルからユーザ名とパスワードを読み込みます。

# login
将棋倶楽部２４へのログインを行い、そのセッション情報を返却するクラスです。
login()でユーザIDとパスワードをloginクラスに設定した後、doLogin()メソッドでログインし、セッションを返却します。

# searchUser
ユーザ検索ページ（https://web.shogidojo.net/24member/meibo/）　をスクレイピングするクラスです。
searchUser()でセッションと検索対象のユーザ名を設定した後、search()で検索を行います。
検索結果はgetMemberSearchResultList()で検索結果を取得できます。
検索結果はmemberSearchResultクラスに格納されます。

# kifuListPage
対局結果一覧ページをスクレイピングするクラスです。

