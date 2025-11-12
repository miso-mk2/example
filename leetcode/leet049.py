class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        lst2 = []
        index_hit = []
        memo = {}

        for i3 in range(len(strs)):
            memo[i3] = sorted(strs[i3])

        #要素数でfor
        for i1 in range(len(strs)):
            if i1 in index_hit:
                continue
            lst1 = [strs[i1]]

            
            #ターゲット以外をfor
            for i2 in range(len(strs)):
                if i2 <= i1:
                    continue

                #文字列をソートして一致するか確かめる
                if memo[i1]==memo[i2]:
                    lst1.append(strs[i2])
                    index_hit.append(i2)
        
            lst2.append(lst1)
        
        return lst2

    
hoge=Solution()

print(hoge.groupAnagrams(["tan","nat","a","atn","kon","nok"]))
print(hoge.groupAnagrams(["a"]))
"""
アナグラムのグループ化
配列で渡される複数の文字列で、同じアルファベットの組み合わせをリストにして返す

配列要素は1~10000
文字列長は0~100
すべて小文字

48分

"""