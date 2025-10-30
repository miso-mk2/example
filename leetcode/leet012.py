class Solution:
    def intToRoman(self, num: int) -> str:

        output=""
        keta =len(str(num)) #桁は文字数なので１桁なら１
        roman = [["I", "V"], ["X", "L"], ["C", "D"], ["M", "?"]]

        #大きい位から順番に見ていく
        for i in range(keta):

            #今何の位か(十なら1 百なら2)
            kurai = keta - i -1 #iは0から始まる
            print(f"位={kurai}")

            #位の数字を取り出す
            num1 = int(str(num)[i])#文字インデックスは0から
            print(f"num1={num1}")

            if num1==9:
                output += roman[kurai][0] + roman[kurai+1][0]
                continue
            
            elif 4 < num1 < 9:
                num1 -= 5
                output += roman[kurai][1]
                
            elif num1==4:
                output += roman[kurai][0] + roman[kurai][1]
                continue
        
            for i2 in range(num1):
                output += roman[kurai][0]

        return output

# test
hoge = Solution()
print(hoge.intToRoman(58))#"LVIII"
print(hoge.intToRoman(1994))#"MCMXCIV"


"""
入力はint整数
出力はstr文字列

1~3999までの整数が入力されるので、
これをローマ数字に変換して出力する

I   1
V   5
X   10
L   50
C   100
D   500
M   1000

"""