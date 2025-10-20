def sum_container(con1):

    if isinstance(con1,dict):
        return sum(con1.values())
    else:
        return sum(con1)

print(sum_container([1,2,3,4,5]))
print(sum_container({"a":1,"b":2,"c":3,"d":4,"e":5}))
print(sum_container((1,2,3,4,5)))
print(sum_container({1,2,3,4,5}))

"""
sum関数を用いれば一行でコンテナの中身を全合計できる
・・・が、ディクショナリだけこの方法だとキーが出てきてダメなので要素を指定するvaluesメソッドを挟む
"""