def kansu(str1,num):
    
    if len(str1) < 2:
        str2= str1
    else :
        str2= str1[:2]

    str3 =""
    for n in range(num):
        str3 += str2

    return str3


print(kansu("asdf",5))
