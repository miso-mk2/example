class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        max_y = len(grid)-1
        max_x = len(grid[0])-1
        #無限大で初期化
        min_sum = float("inf")
        memo = {}

        #再帰
        def saiki(y,x):
            nonlocal min_sum
            sum1=float("inf")
            sum2=float("inf")

            if (y,x) in memo:
                #print("memo使用")
                return memo[y,x]

            #ゴール到達
            if x == max_x and y == max_y:
                return grid[y][x]

            #右を確認して行けそうなら再帰で進む
            if x+1 <= max_x:
                sum1 = saiki(y,x+1)
            #を確認して行けそうなら再帰で進む
            if y+1 <= max_y:
                sum2 = saiki(y+1,x)
            
            min_sum = grid[y][x] + min (sum1,sum2)
            memo[y,x] = min_sum
            
            return min_sum
        #再帰ここまで

        return saiki(0,0)

hoge = Solution()
#print(hoge.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(hoge.minPathSum([[1,2,3],[3,4,6]]))

"""
二次元配列グリッドの左上から右下まで、下か右のみの移動
グリッドには数字が置かれ、その数字の合計が最も小さくなるルートでの、合計値を返す

スタートとゴールは前回同様左上から右下
グリッドサイズは1~200マス
数字は0~200 マイナスは無い

0:47
"""