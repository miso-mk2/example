import os

def kansu(str1):
    if os.path.exists(str1):
        print("発見")
    else:
        print("有効なパスではない")

kansu(__file__)
kansu("test")
kansu("./p108.py")

"""
os.path.exists(パス)
    投入したパスが実在するかどうかを判定する関数
"""