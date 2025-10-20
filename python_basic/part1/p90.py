with open(__file__, 'r') as f:
    source_code = f.read()
    print(source_code)

"""
with
    withブロックは終了したらリソース解放が行われる
    openしたファイルを終了後自動で閉じるために入れると良いらしい
"""