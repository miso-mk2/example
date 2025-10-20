import os,time

print(f"ファイル={__file__}")
print(f"作成日時={time.ctime(os.stat(__file__).st_birthtime)}")
print(f"更新日時={time.ctime(os.path.getmtime(__file__))}")
print(f"閲覧日時={time.ctime(os.path.getatime(__file__))}")
print(f"サイズ={os.path.getsize(__file__)}")

"""
os.path.getsize()
    指定パスのファイルサイズを確認できる関数
"""