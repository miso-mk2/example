class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        output =[]

        #配列をソートすることで、探索方向先の予想がつくようになる
        nums.sort()
        print(nums)

        #一つ目の要素を決めて固定（両面探索が終わったらこれをずらしていく）
        #最後の2周分はLRがすでに十分探索済みかつ、重複探索避けによるエラーを防ぐ
        for indexC in range(len(nums)-2):
            #print(F"for={indexC}")

            #前回のループと同じ数値ならスキップする
            if indexC > 0 and nums[indexC] == nums[indexC-1]:
                continue

            #両端からインデックスで探す
            #indexLをindexCの隣から始めることで同じ重複探索を避ける
            indexL = indexC+1
            indexR = len(nums) - 1

            #二つ目と三つ目の要素を両端から探索
            while indexL < indexR:
                
                #インデックスを動かす
                #ソートしてあるので、Lを動かすと大きくなり、Rを動かすと小さくなる
                #ヒット時は隣の値が同じならスキップして重複を避けつつ、両方のインデックスを動かす
                if nums[indexC] + nums[indexL] + nums[indexR] == 0:
                    output.append([nums[indexC], nums[indexL], nums[indexR]])
                    #print(f"{indexC},{indexL},{indexR}\n    {nums[indexC]},{nums[indexL]},{nums[indexR]}")
                    
                    while indexL < len(nums)-1 and nums[indexL] == nums[indexL+1]:
                        indexL += 1
                    while indexR > 0 and nums[indexR] == nums[indexR-1]:
                        indexR -= 1
            
                    indexL +=1
                    indexR -=1

                elif nums[indexC] + nums[indexL] + nums[indexR] <= 0:
                    indexL += 1
                else:
                    indexR -= 1
                #print(indexL,indexR)

        return output

# test
hoge = Solution()
print(hoge.threeSum([-1,0,1,2,-1,-4]))


"""
三つ以上の整数要素が入った整数配列が入力
・合計するとゼロになる3つの要素PUしてトリプレット（リスト）にする
・すべてのトリプレットを見つけてさらにリストにして返す
    なければ出力無しで終了

・同じトリプレットに同じ要素は使えないが、
・別のトリプレットにはいくら使ってもいい

・配列の順番は気にしなくてい

"""