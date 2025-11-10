class Solution:
    #メモのための変数を用意
    def __init__(self):
        self.memo = {}

    #再帰のために引数を追加　未入力なら0
    def jump(self, nums: list[int],index1: int = 0) -> int:

        index_end = len(nums)

        #末尾なら帰る
        if index1 == index_end - 1:
            return 0

        #このインデックスでの計算がメモしてあるならそちらを利用
        if index1 in self.memo:
            return self.memo[index1]

        #最小ジャンプ回数が要素数を超えることはまずない
        min_count = float('inf')
        
        #先頭を避けて値の数だけforループ（避けた分+1）
        num1 = nums[index1]
        for i1 in range(1,num1+1):
            
            #ジャンプ先のインデックス
            index2 = index1 + i1

            #末尾を超えてるなら無視
            if index2 >= index_end:
                break
            
            #末尾でもなく超えてもいないなら再帰
            count1 = 1 + self.jump(nums,index2)

            #比較して小さい方を保存
            min_count = min(min_count,count1)
            
        #メモする
        self.memo[index1] = min_count

        return min_count

hoge=Solution()
print(hoge.jump([1,1,2,4,1,1,1,1]))
#print(hoge.jump([2,3,1,1,4]))
#print(hoge.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))

"""
配列の先頭から末尾まで、最大で要素の値ずつインデックスを移動（ジャンプ）できる
末尾に到達する最小ジャンプ回数を返せという問題

例）2,3,1,1,4 なら、2からスタートして、3もしくは一個めの1に飛ぶことができる
3に飛べば残りの1,1,4すべてに飛ぶことができ、4に到達すれば終了なので、
最小ジャンプ回数は2回となる

"""