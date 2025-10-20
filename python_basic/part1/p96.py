import traceback

def kansu1():
    kansu2()

def kansu2():
    kansu3()

def kansu3():
    traceback.print_stack()

kansu1()

"""
traceback
    例外発生時の「スタックトレース」を扱うモジュール
スタックトレース
    エラーや例外が発生した時の履歴
traceback.print_stack()
    現在のコールスタックを返す関数
"""