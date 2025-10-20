import socket
def kansu():
    huga = socket.gethostname()
    print(huga)

kansu()

"""
socket
    ネット通信の端部の情報を司るモジュール
    p55にも出てきている
    通信に必要なアドレスとか名前とかが確認できる
"""