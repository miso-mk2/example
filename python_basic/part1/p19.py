def kansuu(str):
    if str[:2]=="is":
        return str
    else:
        return "is"+str

print(kansuu("hoge"))
print(kansuu("ishuga"))