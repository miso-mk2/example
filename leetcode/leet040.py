class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        lst1 = []

        #要素数だけ繰り返す
        for i1 in range(len(candidates)):

            #要素を取りのぞいたリストを作る
            #確認済みの要素（[i]より←の要素）を入れない
            num1 = candidates[i1]
            #print(f"  num1={num1}\ntarget={target}")
            
            #前回と同じ数字なら除外
            if i1>=1 and candidates[i1] == candidates[i1-1]:
                continue

            #ターゲットと要素を比較して超えてるならその枝の探索は不要
            if num1 > target:
                break
            #一致したらその要素を返す
            elif num1 == target:
                lst1.append([num1])
                #print(f"hit {lst1}")

            #ターゲットにまだたりないなら
            #取り除きリストを再起してその中でも組み合わせを作らせる
            else:
                lst2 = self.combinationSum2(candidates[i1+1:],target-num1)
                #[]が帰ってきたらcontinue
                if not lst2:
                    continue

                #帰ってきた取り除き組み合わせリストを最初に取り除いた要素と組み合わせる
                for i2 in lst2:
                    lst3 = [num1] + i2
                    #print(f"lst3={lst3}")
                    lst1.append(lst3)

        #print(f"return={lst1}")
        return lst1

hoge=Solution()
print(hoge.combinationSum2([10,1,2,7,6,1,5],8))
print(hoge.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],10))

"""
合計してターゲットと同じになる一意組み合わせを全部見つける問題
039と違い、同じ数字を使ってはならない

整数や要素数の範囲も039より広いが、
同じ数字が配列に含まれるようになった以外に特別な違いはない

"""