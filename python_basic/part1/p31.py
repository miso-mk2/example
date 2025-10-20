def kansu(x, y):
    result = 1
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            result = k
            break

    return result

print("1,3",kansu(1,3))
print("12,24", kansu(12,24))
print("234,240", kansu(234, 240))
