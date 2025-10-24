from itertools import permutations

#入力を取得
n,x=[int(i)for i in input().split()]
a=[int(i) for i in input().split()]

"""
n=6
x=8
a=[2,1,4,8,1,4]
"""

#print(f"\ninput\n  {n}\n  {x}\n  {a}\n")

lst1 = list(permutations(a))#一旦すべての順列を出力
lst3 = []

for lst2 in lst1 :#一つ一つの順列を検証
    x2=x
    lamp_count = 0

    for num1 in lst2:#順列の中身を頭から確認
        cost = max(0,num1-lamp_count)#ランプを灯した数だけ消費が減るが0より小さくはならない

        if cost > x2:#現在MP(x2)より大きいならこの順列はコピーせず放棄
            #print(f"超過={lst2}")
            break
        
        x2 -= cost
        lamp_count +=1

    else:#最後のランプまで灯すことができたならクリアリストに入れておく
        #print(f" 突破={lst2}")
        lst3.append(lst2)

output=len(lst3)
print(output%998244353)