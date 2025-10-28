#「符号付き32bit整数」が入力される（符号はプラスマイナス）
#符号はそのままに、桁を左右反転する

#例）"123"→"321"　"-543"→"-345"　"120"→"21"
#付け加えて、桁反転によって32bit整数の領域を超える場合は"0"（ゼロ）を返す

class Solution:
    def reverse(self, x: int) -> int:
        
        #マイナスならあとで書き足すので一旦絶対値にして文字列化
        is_minus = True if x < 0 else False
        str1 = str(abs(x))

        #文字列を反転
        str3 = ""
        for str2 in str1:
            str3 = str2 + str3

        #intに変換（マイナスだった場合はマイナスを書き足す）
        if is_minus:
            output = -int(str3)
        else:
            output = int(str3)

        #32bit整数の領域外なら0を返す
        #2**32とかするより実数の方が早いらしい
        if output < -2147483648 or 2147483647 < output:
            return 0

        return output

#テスト入力
hoge=Solution()
print(hoge.reverse(-1234))