import string   #アルファベットa-zA-Zの文字列が入った変数を使う

class Solution:
    def myAtoi(self, s: str) -> int:


        #ーーーすぐ返せるものは返す
        
        #一文字目にあってはならない文字
        jogai1 = string.ascii_letters +"."

        #初期文字列長を保存
        nagasa1 = len(s)

        #すぐ返す判定処理
        if  nagasa1==0 or s[0] in jogai1:
            return 0

        #ーーー先頭のチェックと整理
        
        #先頭空白の個数を確認して除外
        index1 = 0
        while nagasa1 > index1 and s[index1]==" ":
            index1 +=1
        
        #符号のチェックして除外
        is_minus = False
        if nagasa1 > index1 and s[index1] == "-" :
            is_minus =True
            index1 +=1
        elif nagasa1 > index1 and s[index1] =="+":
            index1 +=1
        
        #先頭ゼロの個数を確認して除外
        while nagasa1 > index1 and s[index1]=="0":
            index1 +=1
        
        #符号空白除去して文字がなくなったら０を返す
        if nagasa1 <= index1:
            return 0

        
        #ーーー最も先頭にある整数を文字列で取り出す
        str1=""        
        
        #11桁をこえたら32bit範囲を超えるので終了して良い
        #str型でも一文字なら文字コードで比較が可能
        for num1 in range(11):

            #文字数を超えたらループから出る
            if index1 >= nagasa1:
                break

            #数字をひろう
            if "0" <= s[index1] and s[index1] <= "9":
                str1 += s[index1]
                index1 +=1
                continue
            #数字以外が一番にきたら0を返す
            elif not str1:
                return 0
            #数字以外が出たらループから出る
            else:
                break
            
        #整数型にしてマイナスをつけて出力
        output = int(str1)
        if is_minus:
            output *= -1
        
        #ーーー32bit範囲外なら丸める
        if output < -2147483648:
            return -2147483648
        elif 2147483647 < output:
            return 2147483647
        
        return output

#test用
hoge = Solution()
print(hoge.myAtoi("42"))
print(hoge.myAtoi(" -042"))
print(hoge.myAtoi("1337c0d3"))
print(hoge.myAtoi("-2147483649"))


"""
str型の文字列数字が入力されるので、int型の整数にして返す
文字列には空白やマイナス符号、アルファベットが混ざっているので保存や除去が必要
32bit整数からはみ出したら32bit整数の最大値最小値に丸めて返す

ルールとして
・先頭から読む
・「 」や「-」や「0」は無視して、数字が見つかるまで読む
・↑以外の数字以外の文字が来たら、そこで読み込みを停止する
・空白は文字列の先頭にあるときだけ無視し、それ以外は他の文字と同じく読み込みを停止する
・ハイフンは最初の数字の前にあるときだけマイナスとして扱う（引き算はしない）
・読み込み停止して数字が見つかってない場合は0を返す
・32bit整数版以外なら丸めて返す
・文字列長は0~200

・出てくるのは
    「0-9」「A-Z」「a-z」「+」「-」「 」「.」

"""