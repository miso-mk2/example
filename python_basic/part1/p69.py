
num1 = int(input("整数を入力（1）="))
num2 = int(input("整数を入力（2）="))
num3 = int(input("整数を入力（3）="))

lst1 = [num1,num2,num3]

num_min = min(lst1)
num_max = max(lst1)

num_middle= num1+num2+num3 -num_min -num_max

print(f"{num_min}<{num_middle}<{num_max}")

"min/max関数で値を比較できる"