class Solution:

    def canJump(self, nums: list[int]) -> bool:

        def saiki(nums: list[int],index1: int = 0) -> bool:

            #memoあるならそれを返す
            if index1 in memo:
                return memo[index1]

            #末尾なら帰る
            if index1 == index_end - 1:
                return True
            
            #先頭を避けて値の数だけforループ（避けた分+1）
            num1 = nums[index1]
            #行き止まり
            if num1==0:
                return False
            
            for i1 in range(num1):
                
                #最長ジャンプ先のインデックス（最長から）
                index2 = index1 + num1 - i1
                #print(f"x1={index1} x2={index2} i1={i1} n1={num1}" )
                #進んでないなら帰る
                if index2 == index1:
                    return False

                #末尾を超えてるならクリア
                if index2 >= index_end:
                    return True
                
                #末尾でもなく超えてもいないなら再帰
                bool1 = saiki(nums,index2)
                memo[index1] = bool1

                if bool1:
                    return bool1

            return False
        #再帰ここまで
        
        #要素が一つなら飛ぶ必要もない
        index_end = len(nums)
        if index_end ==1:
            return True

        #０が含まれないなら到達可能
        if not 0 in nums:
            return True
        
        #後ろから0を探索して、それを超えられる要素が一個もなければ到達不可能
        for j in range(index_end):
            #ゼロを見つけたら
            if nums[index_end-1-j]==0:
                print(f"ゼロ発見{index_end-1-j}")
                for k in range(1,index_end-j):
                    print(f"確認{index_end-1-j-k},{index_end-j-k-1 + nums[index_end-j-k-1]}" )
                    if index_end-j-k-1 + nums[index_end-j-k-1] > index_end-j-1 or index_end-j-k-1 + nums[index_end-j-k-1] == index_end-1:
                        print("ゼロを超えられる")
                        break
                else:
                    print("ゼロを超えられない")
                    return False
        
        #上の条件に当てはまり、超えられそうなら実際に超えられるかテスト
        memo = {}
        return saiki(nums)

hoge=Solution()
#print(hoge.canJump([2,3,1,1,4]))
#print(hoge.canJump([3,2,1,0,4]))
print(hoge.canJump([2,0,0]))
#print(hoge.canJump([9,9,9,9,9,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,]))

"""
配列の先頭から末尾まで、最大で要素の値ずつインデックスを移動（ジャンプ）できる
末尾に到達できるか否かをboolで返せという問題

1:35

"""