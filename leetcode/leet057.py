class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #print(intervals)

        output = [newInterval]
        
        for i in range(len(intervals)):
            #new~と重複なく、小さいなら前に挿入、大きいなら後ろに残り全て挿入して終了
            if intervals[i][1] < output[-1][0]:
                output.insert(-1,intervals[i])
            elif output[-1][1] < intervals[i][0]:
                output += intervals[i:]
                return output

            #重複があったら結合
            else:
                output[-1] = [min(output[-1][0],intervals[i][0]),max(output[-1][1],intervals[i][1])]
            #print(f" i={i} output={output} intarv[i]={intervals[i]}")
            
        return output

hoge=Solution()
#print(hoge.insert([[1,3],[6,9],[20,30]],[9,20]))
#print(hoge.insert([[1,2],[3,5],[6,7]],[4,8]))
print(hoge.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[17,18]))


"""

区切られた配列intervalsに、newintervalをねじ込み、重複した場所を結合して返す
intervals自体は重複してなく、順番もソート済み
数字にマイナスはなく、大配列は2個以上 小配列は2個固定

0:48

"""