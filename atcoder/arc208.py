#or判定関数
def or_lst(lst1):
    num1 = 0
    for num2 in lst1: 
        num1 = num1|num2
    return num1

#Xor判定関数
def xor_lst(lst3):
    num3 = 0
    for num4 in lst3:
        num3 = num3^num4
    return num3


#入力をリストに保存
t = int(input())
n = []
a = []
kijun = []

for i in range(t):
    y=int(input())
    n.append(y)
    lst2 = [int(x) for x in input().split()]
    a.append(lst2)

    #or基準を作って保存
    kijun.append(or_lst(lst2))

#print(f" t={t}\n n={n}\n a={a}\n 基準={kijun}\n")

#print(f"ゲーム回数={len(n)}")#ゲーム番号がi2
for i2 in range(len(n)):
    xor_is =False

    #print(f"山の数={len(a[i2])}")#山番号がi3
    for i3 in range(len(a[i2])):

        #print(f"石の個数={a[i2][i3]}")
        a2 = a[i2][:]
        for i4 in range(a[i2][i3]):
            a2[i3] -= 1
            #or判定
            if or_lst(a2)==kijun[i2]:
                #print(" or突破")
                or_is = True
                #勝利系になっているか
                if xor_lst(a2)==kijun[i2]:
                    #print(" xor突破")
                    xor_is =True

        if xor_is :
            break
    #勝敗
    if xor_is :
        print("Alice")
    else:
        print("Bob")

