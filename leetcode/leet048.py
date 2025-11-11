class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat_len = len(matrix)
        
        #print(mat_len)
        #print(matrix)
        
        lst1 = []
        for i1 in range(mat_len):
            lst1.append([])
            for i2 in range(mat_len):
                lst1[i1].append(matrix[mat_len-1-i2][i1])

        #print(lst1)
        matrix[:]=lst1
        

hoge=Solution()
#print(hoge.rotate([[1,2,3],[4,5,6],[7,8,9]]))

huga = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(hoge.rotate(huga))
print(f"huga={huga}")

"""
2D行列を回転させる
リストを書き換えるだけでいいのでreturnの必要はない

    123
    456
    789
    ↓
    741
    852
    963
最小1マス〜最大20マスの正方形
マスに入る数字は-1000〜1000
"""