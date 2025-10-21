str1 = "12345"
str1 = "0" + str1
print(str1)

str2 = "12345"
str2 = str2.rjust(6,"0")
print(str2)

"""
文字列.rjust(桁数,文字) / ljust()
    右詰めないし左詰めで、指定の文字で桁数を揃えるstr型のメソッド
    ゼロ埋めに使ったりできる
"""