class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        max_y = len(obstacleGrid)-1
        max_x = len(obstacleGrid[0])-1
        memo = {}
        #スタート地点が障害物なら帰る
        if obstacleGrid[0][0]==1:
            return 0

        #再帰
        def saiki(y,x):
            
            #memo使用
            if (y,x) in memo:
                return memo[y,x]
            
            num1 = 0

            #ゴール到達
            if x == max_x and y == max_y:
                return 1

            #右を確認して行けそうなら再帰で進む（範囲外でなく、障害物もない場合）
            if x+1 <= max_x and obstacleGrid[y][x+1]==0:
                num1 += saiki(y,x+1)
            #を確認して行けそうなら再帰で進む
            if y+1 <= max_y and obstacleGrid[y+1][x]==0:
                num1 += saiki(y+1,x)
            
            #メモ保存
            memo[y,x] = num1
            return num1
        #再帰ここまで

        return saiki(0,0)

hoge = Solution()
print(hoge.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
#print(hoge.uniquePathsWithObstacles([[1,0],[0,0]]))

"""
二次元配列グリッドの左上から右下まで、下か右のみの移動で到達するパターンの数
グリッドには障害物が置かれ、それを避けたパターン数を返す必要がある

[0,0,0],[0,1,0],[0,0,0]なら
◻︎◻︎◻︎
◻︎◼︎◻︎
◻︎◻︎◻︎

スタートとゴールは前回同様左上から右下
グリッドサイズは1~100マス
障害物は複数となるが、到達不可能のパターンがあるかどうかは書かれていない

0:53

"""