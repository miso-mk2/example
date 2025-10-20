import sys

if sys.maxsize > 2147483647 :
    print("64bit")
else:
    print("32bit")

"配列の最大要素数を確認するメソッド 32bitの限界数より大きいなら64bit"