import time

print(time.ctime())

print(time.time())
print(time.ctime(time.time()))

"""
time.ctime()
    時間データをフォーマットする用途で用いる機会が多いが、
    引数を省略するとtime()が返すシステム時間がフォーマットされた状態で出てくる
"""