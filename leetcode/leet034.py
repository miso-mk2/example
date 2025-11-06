class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #print(nums)

        num1 = len(nums)

        #無なら
        if not num1 :
            return [-1,-1]

        #targetの先頭と末尾を探索する
        for i in range(2):
            print(f"for={i}")

            #両端のインデックス
            low,high = 0,num1-1
            while low<=high:

                #中央のインデックス
                mid = (high+low)//2
                print(f" low={low}\n mid={mid}\n high={high}\n")

                if i ==0:#先頭探索
                    if nums[mid]==target and (mid ==0 or nums[mid-1] < nums[mid]):
                        break
                    elif nums[mid] < target:
                        low = mid +1
                    else:
                        high =mid -1
                else:#末尾探索
                    if nums[mid]==target and (mid ==num1-1 or nums[mid] < nums[mid+1]):
                        break
                    elif nums[mid] <= target:
                        low = mid +1
                    else:
                        high =mid -1
        
            #先頭と末尾を記録（一致しなかったら-1）
            if i ==0 and nums[mid] == target:
                sentou = mid
            elif i==0:
                sentou = -1
            elif nums[mid] == target:
                matubi = mid
            else:
                matubi= -1

        #print(sentou,matubi)
        return [sentou,matubi]

hoge=Solution()
print(hoge.searchRange([5,7,7,8,8,10],10))

"""
「非減少順」でソートされた配列からターゲットを探す
同じ数字が複数並ぶので、その開始〜終了のインデックスを返す

"""