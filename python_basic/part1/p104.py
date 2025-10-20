import os

print(f"実効グループID={os.getegid()}")
print(f"実効ユーザーID={os.geteuid()}")
print(f"ID={os.getgid()}")
print(f"補足グループ={os.getgroups()}")

"""
os.getegid()
    ゲットエフェクティブグループIDの略
これらのIDにファイルへのアクセス権限とかが紐づいてる

"""