import itertools

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        lst1 = list(itertools.permutations(nums))
        return lst1

hoge=Solution()
print(hoge.permute([1,2,3]))

"""
配列から全順列を作れという問題
"""