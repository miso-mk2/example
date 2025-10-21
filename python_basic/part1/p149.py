limit = 5

def kansu(lst1):

    lst2 = [num1**3 for num1 in lst1 if num1<=limit]

    output = sum(lst2)
    return output

print(kansu([1,4,6,7]))
