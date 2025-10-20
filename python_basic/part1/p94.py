str1 ="hello"
code1 = str1.encode()

print(code1)
print(list(code1))

"""
.encord("文字コード")
    指定した文字コードにエンコードするメソッド
    文字コードはデフォルトだとUTF-8
    b'[文字列]' という形で表示される
    これをリストで分けると整数になる
"""