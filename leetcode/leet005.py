#数字と英語のみの文字列が入力
# 最長の「回文」を抽出して出力する

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #とりあえず入力がまるごと回文ならそのまま返す
        if s==s[::-1]:
            print("-0")
            return s

        for i1 in range(len(s)):
            num1=i1
            num2=0

            #スライスで両側から削ってチェックして
            for i2 in range(i1+1):

                if num2 < 1:
                    str1=s[num1:]#末尾指定を空欄にしないと末尾が拾えない
                else:
                    str1=s[num1:-num2]

                #回文チェック 通ったらブレイクもせず関数自体を終了
                if str1==str1[::-1]:
                    return str1
                
                #削り位置を前から後へずらしていく
                num1-=1
                num2+=1




#test入力
hoge=Solution()
print(hoge.longestPalindrome("12345432"))
#print(hoge.longestPalindrome("babad"))