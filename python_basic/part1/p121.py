
#hoge = "huga"

try:
    print(hoge)
except NameError:
    print("「hoge」は変数として存在しません")
else:
    print("「hoge」は変数として存在します")

"""
try-except文にはelseブロックも用意できる
"""