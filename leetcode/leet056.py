class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        #二次元配列を小配列の先頭でソートする
        intervals.sort(key=lambda x: x[0])
        output = []
        num_len = len(intervals)

        for i in range(num_len):
            lst1 = intervals[i]

            if not len(output):
                output.append(lst1)
                continue
            
            for j in range(len(output)):
                #print(f"j={j}")

                #j個前の配列の末尾がターゲット先頭より大きい場合は結合（もしくは入れ替え）
                if output[-1-j][1] >= lst1[0]:
                    #print("上書き")
                    #一個前より完全に小さくて重複してない場合は一個前に挿入
                    if lst1[1] < output[-1-j][0]:
                        output.insert(len(output)-1,lst1)
                    else:                
                        #末尾を上書きするか否か
                        if output[-1-j][1] < lst1[1]:
                            output[-1-j][1] = lst1[1]
                        #先頭を上書きするか否か
                        if output[-1-j][0] > lst1[0]:
                            output[-1-j][0] = lst1[0]
                elif j==0:
                    #print(f"lst1={lst1}")
                    output.append(lst1)
                    break

        return output

hoge=Solution()
#print(hoge.merge([[1,3],[2,6],[8,10],[15,18]]))
#print(hoge.merge([[1,4],[4,5]]))
print(hoge.merge([[3,4],[1,2],[4,7]]))
print(hoge.merge([[2,3],[4,5],[6,7],[5,10]]))
"""
区切られた配列から重複区間を結合する
[[1,2],[3,4],[4,5],[6,7]]→ [[1,2],[3,5],[6,7]]
"""