def kansu(arg1):

    if isinstance(arg1,int):
        print("整数")
    elif isinstance(arg1,str):
        print("文字列")
    else:
        print("その他")

kansu(1)
kansu("1")
kansu([1])

"""
isinstance(変数,型)
    変数が指定の型と一致するかどうかを返す関数
    typeより柔軟で「文字列だけどサブクラスが整数」みたいなのもtrueを返せる
"""