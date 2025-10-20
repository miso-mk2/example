import cProfile

def kansu():
    print("test")
print(kansu())

cProfile.run("kansu()")

"cprofile.runで関数の利用頻度などを確認できる"