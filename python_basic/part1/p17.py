def kansuu(num):
    return ((abs(1000 - num) <= 100) or (abs(2000 - num) <= 100))

print(kansuu(1020))
print(kansuu(1909))
print(kansuu(1899))
