class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        lst1 = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        num1 = len(digits)
        print(num1)

        output = []
        for i in lst1[int(digits[0])]:
            if num1 > 1:
                for j in lst1[int(digits[1])]:
                    if num1 >2:
                        for k in lst1[int(digits[2])]:
                            if num1 >3:
                                for l in lst1[int(digits[3])]:
                                    output.append(i+j+k+l)
                            else:
                                output.append(i+j+k)
                    else:
                        output.append(i+j)
            else:
                output.append(i)

        return output


# test
hoge = Solution()
print(hoge.letterCombinations("2"))



#メモ化
#for文を大量に使えば一応動きそうではある
"""
アメリカ企業のCMとかに出てくる電話番号を対応するアルファベットで英単語にする変換
2~9までの数字が最大4桁 str型で入力されるので、
その数字が示す可能性のあるアルファベットの組み合わせを全て書き出してリストで出力する
"""
