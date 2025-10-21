def kansu(lst1):

    lst2 = [num1 for num1 in lst1 if num1 %2 !=0]

    if len(lst2) >= 2:
        return True
    else:
        return False

print(kansu([1,2,3,4,5,6]))
print(kansu([2,3,4,6]))
print(kansu([2,4,6,8,10]))