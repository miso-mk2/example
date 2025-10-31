class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        
        #配列をソートすることで、探索方向先の予想がつくようになる
        nums.sort()
        #前回の差を格納する変数　一周目で空だと困るので頭の３個を適当に入れておく
        num2 = nums[0]+nums[1]+nums[2]
        #print(nums)
        
        #一つ目の要素を決めて固定（両面探索が終わったらこれをずらしていく）
        #最後の2周分はLRがすでに十分探索済みかつ、重複探索避けによるエラーを防ぐ
        for indexC in range(len(nums)-2):
            #print(F" for={indexC}")

            #前回のループと同じ数値ならスキップする
            if indexC > 0 and nums[indexC] == nums[indexC-1]:
                continue

            #両端からインデックスで探す
            #indexLをindexCの隣から始めることで同じ重複探索を避ける
            indexL = indexC+1
            indexR = len(nums) - 1

            #二つ目と三つ目の要素を両端から探索
            while indexL < indexR:
                #print(f"  while={indexR}")


                #合計を保存
                num1 = nums[indexC] + nums[indexL] + nums[indexR]

                #近いなら保管
                if abs(num1-target) < abs(num2-target):
                    num2 = num1

                #判定
                if num1 == target:#合計がターゲットと一致したら関数終了
                    return target
                elif num1 < target:#ターゲットより小さいならLを移動
                    indexL += 1
                elif num1 > target:#ターゲットより大きいならRを移動
                    indexR -= 1

        return num2
    

# test
hoge = Solution()
#print(hoge.threeSumClosest([-1,2,1,-4],1))
#print(hoge.threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2))
#print(hoge.threeSumClosest([1,1,1,0],-100))
print(hoge.threeSumClosest([1,1,1,5,5,5,5,5,5],14))


"""
三つ以上の整数要素が入った整数配列 と、ターゲットの整数が入力される
合計するとターゲットに最も近くなる3つの要素を見つけて合計して返す

"""
