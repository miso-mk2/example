class Solution:

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        output = []

        for i in range(len(nums)-3):
            print(i)
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)-2):
                if   j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                indexL=j+1
                indexR=len(nums)-1

                while indexL < indexR:

                    sum1 = nums[i]+nums[j]+nums[indexL]+nums[indexR]

                    if sum1 == target:
                        output.append([nums[i], nums[j], nums[indexL], nums[indexR]])

                        while indexL < indexR and nums[indexL] == nums[indexL + 1]:
                            indexL += 1
                        while indexL < indexR and nums[indexR] == nums[indexR - 1]:
                            indexR -= 1
                        
                        # 次の組み合わせへポインタを移動
                        indexL += 1
                        indexR -= 1
                    
                    elif sum1 < target:
                        indexL += 1 # 和を大きくするために indexL を右に移動
                    else:
                        indexR -= 1 # 和を小さくするために indexR を左に移動

        return output

hoge = Solution()
print(hoge.fourSum([1,0,-1,0,-2,2],0))
print(hoge.fourSum([2,2,2,2,2],8))



"""
配列の要素を４つ合計して、ターゲットと一致する「組み合わせ」を全て答える
順不同 要するに重複は禁止
"""