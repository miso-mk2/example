class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #print(nums)
        
        sum1 = 0
        max_sum = 0

        #先頭から全部見ていく
        for i1 in range(len(nums)):
            #print(f"i1={i1}")

            #先頭を探す
            if not max_sum:
                #プラスでないならスキップ
                if nums[i1] < 0:
                    continue
                else:
                    max_sum = nums[i1]
                    sum1 = nums[i1]
                    continue
            else:
                #先頭と今の要素を足して、プラスなら足す
                if sum1 + nums[i1] > 0:
                    sum1 += nums[i1]
                    #今までで一番大きいなら保存
                    if max_sum < sum1:
                        max_sum = sum1
                #マイナスになったら
                else:
                    sum1 = 0
        
        if max_sum == 0:
            return max(nums)
    
        return max_sum


hoge=Solution()

#print(hoge.maxSubArray([0,1,2,3,-8,6]))
#print(hoge.maxSubArray([0,1,2,3,-7,8]))
#print(hoge.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#[4,-1,2,1,]
#print(hoge.maxSubArray([0,-8,-3,-5,-1,-6]))
#print(hoge.maxSubArray([-54]))
print(hoge.maxSubArray([5,4,-1,7,8]))

"""
符号付き整数配列の中から、合計して最大になる部分を切り出して合計を返す

0:55
"""