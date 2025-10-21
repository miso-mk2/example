
def kansu(lst1):
    num_max = lst1[0]
    num_min = lst1[0]
    
    for num1 in lst1:

        if num1 > num_max:
            num_max = num1

        elif num1 < num_min:
            num_min = num1
    
    return num_max, num_min

print(kansu([1,2,3,5,6,-7,8,2]))
