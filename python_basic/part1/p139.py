import ipaddress

def kansu(str1):
    try:
        ipaddress.ip_address(str1)
        return True
    except ValueError:
        return False

print(kansu("192.168.1.255"))
print(kansu("192.168.1.256"))

"""
ipaddress
    IPアドレス関係のモジュール
    address型オブジェクトを扱う
    アドレスの検証や操作ができる
.ip_address()
    文字列がIPアドレスとして有効な形式ならaddress型オブジェクトに変換する
    今回はtry-except文で有効かどうかの判定に使うのみ
"""