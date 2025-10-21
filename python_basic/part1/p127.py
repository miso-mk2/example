def kansu(num1):
    num_max = 2**64 -1
    num_min = -2**64
    if num_min <= num1 <= num_max:
        return True
    else:
        return False

print(kansu(500))
print(kansu(2**64))