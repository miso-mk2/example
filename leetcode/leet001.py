
#numsに配列 targetに整数が入力される
#配列の内からどれか二つの要素を合計して、targetと一致する数字にする。
#一致した配列のインデックスをリストで出力するインスタンスメソッドを作れ、という問題
#回答はprint()のstdput（標準出力）ではなく、returnのoutput(出力)で行う
#numsの要素数は最大１万個　投入される整数並びにターゲットはマイナスもありうる

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        print(target)
        
        for idx1,num1 in enumerate(nums):
            for idx2,num2 in enumerate(nums):
                if idx1 == idx2 :
                    continue
                if num1 + num2 == target:
                    return [idx1,idx2]
                    
