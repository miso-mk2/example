import os

print(__file__)
print(os.path.abspath(__file__))

"__file__だけだと環境によっては相対パスになったりするらしい"