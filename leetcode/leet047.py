class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        num_len = len(nums)
        lst1 = []
        lst3 = []

        #再帰で繰り返す
        def saiki(lst2):

            #末尾に達してたらlst2の結果をlst1に保存する処理
            if len(lst2) == num_len:
                lst1.append(tuple(lst2[:]))
                return

            #今の値をlst2に入れていく処理
            for i1 in range(len(nums)):

                if i1 not in lst3:
                    #値を保存しつつ、使用済みインデックスもlst3に保存
                    lst3.append(i1)
                    lst2.append(nums[i1])

                    saiki(lst2)

                    #帰ってきたらその値とインデックスはlstから取り除く
                    lst3.pop()
                    lst2.pop()

            return

        saiki([])
        
        #setに変換して重複を消す
        lst1 = set(lst1)
        lst2 = [list(i2) for i2 in lst1]
        return list(lst2)


hoge=Solution()
#print(hoge.permuteUnique([3,1,2]))
print(hoge.permuteUnique([1,1,2]))

"""
ダブりのある配列からダブりのない全順列を作れという問題
"""