def kansu(str1):
    if str1.isupper():
        return False
    else:
        return True

print(kansu("HELLO"))
print(kansu("Hello"))
print(kansu("hello"))

"""
「文字列」.isupper()/.islower()
    文字列に大文字/小文字が含まれているか判定するstr型のメソッド
    今回は一文字でも含まれていればアウトにする為isupper
"""