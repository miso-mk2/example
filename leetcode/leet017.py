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
"""

文字数で必要な要素数を出して数字そのままのリストを先に作っておいて
入力文字列の頭から特定の数字を変換というのもありか?
7と9が4文字なのが痛い

普通に8種の組み合わせをリストで作っておく
文字数でfor文回して頭からリスト作成
n文字目で増えるリストをどう対処するか

1桁なら3個
2桁なら9個3桁27個で
4桁81個の要素になる（79がなければ）
全部79の4文字だったら256個か

頭から読んでいくとして、一桁目の時点では3個しか要素を作らないなら、
二桁目の時にどうやって増やせばいいのかというところ

a b c
↓
aaa bbb ccc
↓
adaeaf bdbebf cdcecf

いやぁちょっと全然思いつかん
今頭回ってない

あ〜再帰呼び出しで
最初に呼び出したやつ（ルート）が自分を３個再起して、
再起先がさらに３個再起して
最後の桁ならリストを作って文字入れて返して
帰ってきたリストに文字入れて返して
で作れる・・・のか？

んんん？

あ、
for 1文字目 abcの3回
    i
    for 2文字目 defの3回
        j
        for 3文字目 ghiの3回
            k
            str += i+j+k

        


"""