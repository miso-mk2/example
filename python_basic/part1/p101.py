import http.client

hoge = http.client.HTTPConnection("example.com")
hoge.request("GET", "/")
print(hoge.getresponse().read())


"""
http.client
    httpプロトコルクライアント機能を提供するモジュール
    ウェブ上の情報の取得したりできる

HTTPConnection("URL")
    http.clientモジュールに含まれる、リクエストを送受信する関数
    ここのURLに"http"などは不要（しかしhttpsの場合は別の関数が必要なので無視ではない）

.request("GET","/")
    HTTPConnectionの、「送信」を担当するメソッド

.getresponse()
    HTTPConnectionの、「受信」を担当するメソッド
    そのままでは読めないのでread()関数もつけている
"""