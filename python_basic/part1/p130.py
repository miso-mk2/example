import json

str1= '"test"'
print(str1)

dic1 = {"a":1,"b":2,"c":3}
print(dic1)
print(json.dumps(dic1))

"""
jsonモジュール
    jsonファイルやjsonデータを処理するための機能をまとめたモジュール
json.dumps()
    コンテナをjsonデータに書き換える関数
"""