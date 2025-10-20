import os , time

paths = ["%s %s" % (time.ctime(t), f) for t, f in sorted([(os.path.getctime(x), x) for x in os.listdir(".")])]

for x in range(len(paths)):
    print(paths[x],)

"""
"%s %s" % (「対象」,「対象」)
    文字フォーマット 間にスペースを開けて対象に置き換える
os.listdir()
    指定したディレクトリのファイルやディレクトリをリストで返す
sorted()
    ソートする sort()と違い元データを変更しない

[（処理）for 変数 in 配列 ]
    リスト内包表記型for文 このfor文そのものをリストとして使用可能となる    

検索したパスのリストの回数分、ファイルの更新時間を取得してソートした文字列を生成して、
それもリストにした上で表示している
"""