import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        output = math.factorial(m-1+n-1)//(math.factorial(m-1)*math.factorial(n-1))
        return output

hoge = Solution()
print(hoge.uniquePaths(3,7))

"""
m*nグリッドの左上から右下まで、下か右のみの移動で到達するパターンの数

移動回数合計の階乗 / ((縦移動回数の階乗)*(横移動回数の階乗))

0:42

"""