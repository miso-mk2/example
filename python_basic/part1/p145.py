def kansu(arg1):

    if isinstance(arg1,list):
        print("リスト")
    elif isinstance(arg1,tuple):
        print("タプル")
    elif isinstance(arg1,set):
        print("セット")
    else:
        print("その他")

kansu([1,2,3])
kansu((1,2,3))
kansu({1,2,3})
kansu("hoge")