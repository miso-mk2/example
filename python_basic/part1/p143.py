import sys

if sys.maxsize > 2**32:
    print("64bit")
else:
    print("32bit")