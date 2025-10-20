def kansu(num1,num2):
    if num1==num2 or num1+num2==5 or abs(num1-num2)==5:
        return True
    else :
        return False


print(kansu(2,7))
print(kansu(2,3))
print(kansu(2,2))
print(kansu(2,1))