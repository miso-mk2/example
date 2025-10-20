import os ,time
print(f"作成日時={time.ctime(os.stat("p64.py").st_birthtime)}")
print(f"更新日時={time.ctime(os.path.getmtime("p60.py"))}")

"macとunixで「ファイル作成日時」の格納場所が違う模様"