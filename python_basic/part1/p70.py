import glob,os

list1 = glob.glob("../../*.txt")

print(f"名前順{list1}")
list1.sort(key=os.path.getmtime)
print(f"時間順{list1}")

"sort関数メソッドはリストの要素を比較して並べ替える"
"要素の名前だけで無く、どこを比較するかを引数keyで指定可能"