import sys
print("スクリプトのパス=", sys.argv[0])
print("引数の数=", len(sys.argv))
print("引数のリスト:", str(sys.argv))

"""
「python3 p76.py arg1 arg2 arg3」
↑これをターミナルで実行すると↑↑が実行される
sysモジュールargvメソッドでこうしてスクリプト自身の情報が確認できる
"""