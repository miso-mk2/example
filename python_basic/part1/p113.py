def checkkansu(str2):
    try:
        int(str2)
        return "整数です"
    except ValueError:
        return "整数ではありません"

str1 = input("数値を入力=")
print(checkkansu(str1))

"""
try - except文
    通常、構文エラーが発生したら処理は止まってしまうが、
    tryブロックでエラーが発生しても全体は止まらず、
    exceptブロックに分岐して処理が続けられる
    except文はエラーの種類を指定可能

"""