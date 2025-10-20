import os

def dirfile_check(path1):
    if os.path.isdir(path1):
        return "dir"
    elif os.path.isfile(path1):
        return "file"
    else:
        return "othr"

print(dirfile_check("./p85.py"))
print(dirfile_check("../part1"))
print(dirfile_check("hoge"))

"""
os.path.isdir/isfile([パス])
    調査対象のパスが「ファイル」か「ディレクトリ」かを判定できるモジュールメソッド
"""