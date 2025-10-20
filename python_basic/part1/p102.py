import subprocess

print(subprocess.check_output(["ls","-l"],text=True))

"""
subprocess
    p45でもやったターミナルを操作できるモジュール

subprocess.check_output("ターミナルコマンド",表示のオプション)
    ターミナルのコマンドを実行しつつ、その結果を取得する
    コマンドは一つ一つ括って送る必要があるっぽい
    「text = True」は改行とかして読みやすくしてくれる
"""