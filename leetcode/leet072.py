from functools import lru_cache

class Solution:
    #再帰関数用のメモ化モジュール
    @lru_cache(maxsize=4096)
    def minDistance(self, word1: str, word2: str) -> int:

        #片方が空なら長い方の文字数を返す
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        #一致ならコストを加算せず（+1されない）、再起で次にすすむ
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        #挿入
        #端まで削って見つからないならword1の残り文字列数が返ってくる
        l1 = self.minDistance(word1, word2[1:])
        #削除
        l2 = self.minDistance(word1[1:], word2)
        #変換
        l3 = self.minDistance(word1[1:], word2[1:])

        #三種の選択肢の中で最も操作が少なかったものを採用して返す
        return 1 + min(l1, l2, l3)

hoge=Solution()
#print(hoge.minDistance("horse","ros"))
print(hoge.minDistance("012345","12356"))

"""
1つ目の文字列を変換して2つ目の文字列にする際に必要な操作回数
操作は一文字ずつ「変換」「削除」「挿入」が可能
文字は全て小文字で0~500文字

〜〜〜〜

文字列同士を頭から比較し、
三種の操作を行なって「一致させた」扱いになったらインデックスを削っていく
最終的なword1と2のインデックスのズレ（差）が削除挿入の操作回数として計上され
一致を多く作って操作の数を減らし、削除と挿入のバランスをとれる選択肢がもっとも操作回数が少ないと言える

3:10
"""