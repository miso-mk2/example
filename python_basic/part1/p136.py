import pathlib

def kansu(str1):
    
    path1 = pathlib.Path(str1)
    lst1 = [path2.name for path2 in path1.iterdir() if path2.is_file()]
    return lst1

print(kansu("."))

"""
pathlibモジュール
    ファイルパスをオブジェクトとして扱うためのモジュール
pathlib.path(指定のファイルパス)
    ファイルパスからpath型オブジェクトを作る
.name
    path型に格納されてるファイル名だけの変数
.iterdir()
    path型ディレクトリの中身を配列として返す
    中の要素もpath型オブジェクトとして取り出せる
.is_file()
    path型オブジェクトがファイルか否かを判定する
[処理 for 変数 in 配列 if 条件]
    条件付きリスト内包表記型for文
    末尾に付け加えた条件を満たさない場合は処理を飛ばす
"""