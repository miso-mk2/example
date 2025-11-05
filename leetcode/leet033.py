class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #print(nums)
        
        #ソート（真先頭探索）
        #要素数確認（3個以下ならソート不要）
        num1 = len(nums)
        if num1 <= 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        
        else:            
            #先頭末尾にポインタ
            low, high = 0, num1 - 1

            #ポインタがぶつかるまでループ
            while low <= high:
                
                #真ん中にmidポインタ
                mid = (low + high) // 2
                
                #ズレがないならソート不要
                if nums[low] <= nums[high]:
                    sentou = low
                    break
                
                #midの右隣がmidより小さいならそれが真先頭
                if nums[mid] > nums[mid + 1]:
                    sentou = mid + 1
                    break
                #midの左隣がmidより大きいならmidが真先頭
                if nums[mid-1] > nums[mid]:
                    sentou = mid
                    break

                #low<mid<highが崩れている方に真先頭がある
                if nums[mid] >= nums[low]:
                    low = mid + 1
                else:
                    sentou = mid
                    high = mid - 1

            #真先頭から左右を入れ替えて正しい配列に直す
            nums = nums[sentou:] + nums[:sentou]
    
        #探索
        #先頭末尾にポインタ
        low, high = 0, num1 - 1
        #見つからなかった時は-1を返す
        indexT = -1

        #ポインタがぶつかるまでループ
        while low <= high:

            #真ん中にmidポインタ
            mid = (low + high) // 2
            
            #ターゲット発見なら
            if nums[mid] == target:
                indexT = mid + sentou if mid+sentou < num1 else mid+sentou - num1
                break

            #low<mid<highが崩れている方に真先頭がある
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        #print(f"indexT={indexT}")
        #print(nums)
        return indexT

hoge=Solution()
print(hoge.search([4,5,6,7,0,1,2],4))
#print(hoge.search([4,5,6,7,8,1,2,3],8))

"""
targetを配列から見つけてインデックスを返せ
ない場合は-1を返せ

計算量 O(log(n))に収めること

"""