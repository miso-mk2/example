class Solution:
    def countAndSay(self, n: int) -> str:

        output = "1"
        str1 = ""

        #指定の繰り返し回数RLEを行う
        for i1 in range(n-1):
            
            #今の文字数を確認
            num1 = len(output)

            #文字数で頭から確認し繰り返しカウントを行う
            count1= 1
            for i2 in range(num1):
                #print(f"i2={i2}")

                #末尾、もしくは隣の文字が同じでないなら
                # 文字列を作成しカウントをリセット
                if i2 >= num1-1 or not (output[i2]==output[i2+1]):
                    str1 += str(count1) + output[i2]
                    count1 = 1
                #隣の文字が同じならカウント+1
                else:
                    count1 +=1
                    continue

            output = str1
            str1 = ""
            #print(f"out={output}")

        return output

hoge=Solution()
print(hoge.countAndSay(8))

"""
RLE：ランレングスエンコード
    データ圧縮方式
    1111→41 1が4回という意味
    同じデータが並びやすい画像などを圧縮する際に使われる

「1」をn回ランレングス圧縮する
最大30回

"""