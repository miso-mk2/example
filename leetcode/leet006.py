#文字列一行[s]
# 変数[numRows]（１〜１００の整数）が入力される
#「内部的に変数の高さのジグザグに並べ替えて」「それを横読み」して
#順番がバラバラになった文字列を出力する

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        #毎回関数で確認する必要はないので変数に入れておく
        str_length = len(s)

        #そのまま返していいパターンはそのまま返す
        if numRows ==1 or numRows >= str_length:
            return s

        #出力用変数を用意
        str1=""

        #インデックス操作用の変数を用意
        #上折り返しとした折り返しがあるので二つ用意
        interval1 = numRows*2-2
        interval2 = 0

        #numRowsの段数の回数ループ
        for f2 in range(numRows):
            print(f"for({f2}")

            #この変数で文字列を指定して出力する
            index1 = f2
            str1 += s[index1]
            
            count =0 #while回数カウンター

            #whileで横読みの文字数ループ
            while True:

                #出力変数にインデックスで指定した位置の文字を書き足す
                #折り返しのタイミングでは文字を書き足さない
                if (count%2 ==0 and interval1 < 1) or (count%2 !=0 and interval2 < 1):
                    count+=1
                    continue

                #インデックス操作
                #奇数ループと偶数ループで進む間隔を変える
                elif count%2==0:
                    index1+= interval1
                else:
                    index1+= interval2

                #文字列長より先のインデックスを指定しようとしてたら
                #右端に到達した証なので、ループから出る
                if index1 >= str_length:
                    break

                #文字列を作成
                str1 += str(s[index1])

                #while回数カウンター
                count +=1
            
            #折り返し間隔を変更
            interval1 -=2
            interval2 +=2

        return str1


#テスト入力
hoge=Solution()
print(hoge.convert("AB",3))
#print(hoge.convert("01234567890123456789",5))

"""
例として
入力）01234567890123456789 ,5
    ↓
0     8     6
1   7 9   5 7
2  6  0  4  8
3 5   1 3   9
4     2

    ↓
出力）08617957260483513942
となる
"""