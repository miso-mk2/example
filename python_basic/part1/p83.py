def bigger_n(lst1):
    n=3
    if all(num > n for num in lst1):
        return True
    else:
        return False

print(bigger_n([4,5,6,7,8]))
print(bigger_n([4,5,6,7,3]))

"""
all([条件式][for文])
    要素すべてが条件に合ってれtrueを返す
"""