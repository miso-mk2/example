def kansu(list1, num1):
    for num2 in list1:
        if num1 == num2:
            return True
    return False

print(kansu([1,5,8,3],3))
print(kansu([5,8,3],-1))

