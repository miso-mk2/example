def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z

    return sum

print(sum(2,2,5))
print(sum(5,5,5))
print(sum(1,2,3))
