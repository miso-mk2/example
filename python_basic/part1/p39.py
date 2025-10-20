def kansu (amt,int,year):
    return  amt*((1+int/100)**(year))

print(kansu(10000,3.5,7))
