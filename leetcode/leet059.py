class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        
        output = []
        x = 0
        y = 0
        houkou = 0

        max_x = n
        max_y = n
        min_x = 0
        min_y = 0


        for i in range(n):
            output.append([0 for j in range(n)])

    
        for i in range(1,n*n+1):
            #print(f" x={x} y={y} output={output}")
            
            output[y][x] = i
            
            if houkou == 0:
                x += 1
                if x >= max_x:
                    x -= 1
                    y += 1
                    houkou += 1
                    min_y += 1
            elif houkou == 1:
                y += 1
                if y >= max_y:
                    x -= 1
                    y -= 1
                    houkou += 1
                    max_x -= 1
            elif houkou == 2:
                x -= 1
                if x < min_x:
                    x += 1
                    y -= 1
                    houkou += 1
                    max_y -= 1
            else:
                y -= 1
                if y < min_y:
                    x += 1
                    y += 1
                    houkou = 0
                    min_x += 1

        return output

hoge=Solution()
print(hoge.generateMatrix(4))


"""
入力n
n*nの二次元配列を生成する
ただし、順番は渦巻き型

n=3
123
894
765

0:38
"""