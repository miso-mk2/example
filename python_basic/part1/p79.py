import sys

str1 =1
str2 ="1"
str3 ="11111111"

print(f"{sys.getsizeof(str1)}バイト")
print(f"{sys.getsizeof(str2)}バイト")
print(f"{sys.getsizeof(str3)}バイト")

"""
sys.getsizeof(object[, default])
    指定したオブジェクトのサイズをバイト数で返す

"""