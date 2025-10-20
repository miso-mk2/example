def kansu(x, y):
    result = 1
    if x > y :
        z = x
    else:
        z= y
    
    while True :
        if (z % x == 0) and (z % y == 0):
            result =z
            break
        z+=1

    return result

print("1,3",kansu(1,3))
print("12,24", kansu(12,24))
print("234,240", kansu(234, 240))