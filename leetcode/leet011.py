class Solution:
    def maxArea(self, height: List[int]) -> int:

        #最大面積を保存する変数
        output = 0

        #両端からインデックスで探す
        indexL = 0
        indexR = len(height) - 1

        while True:
            #左右のインデックスがぶつかったら探索を終了する
            if indexL > indexR: 
                break
            
            #現在の高さ
            if height[indexL] > height[indexR]:
                now_height = height[indexR]
            else:
                now_height = height[indexL]
            
            #現在の幅
            now_width = indexR - indexL
            now_area = now_height * now_width

            #面積が大きかったら保存
            if output < now_area:
                output = now_area
            else:
                output = output
            #print(output,now_area)

            #短い方のインデックスを動かす
            if height[indexL] < height[indexR]:
                indexL += 1
            else:
                indexR -= 1

        return output

# test
hoge = Solution()
print(hoge.maxArea([1,8,6,2,5,4,8,3,7]))
print(hoge.maxArea([1,1]))


"""
入力は整数配列list[int]
出力はint

配列のインデックスをX軸
配列要素の値をY軸として、
一番大きな面積の長方形を作れる(水を貯めれる)二つの要素を選んで、
低い方の高さとインデックス幅の面積を返す

配列要素の整数にマイナスはでない
要素数は最低２個

"""
