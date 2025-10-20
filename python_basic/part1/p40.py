import math

def kansu(lst1,lst2):

    return math.sqrt(((lst1[0]-lst2[0])**2)+((lst1[1]-lst2[1])**2))

print(kansu([4,0],[6,6]))

"mathモジュールのルート2メソッドで2点の座標を割り出す"