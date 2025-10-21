
def kansu(str1):
    
    num1 = 0
    for str3 in str1:

        if str3 == '0':
            num1 += 1
        elif num1 > 0:
            num1 -= 1
    
    if num1 == 0:
        return True
    else:
        return False

print(kansu("01010101"))
print(kansu("00"))
print(kansu("000111000111"))
print(kansu("00011100011"))
