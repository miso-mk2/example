#文字列が入力される（アルファベットと数字と記号とスペース）
#同じ文字が重複しない、最長の文字列を見つけてその長さを整数で出力する

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #空が入力されるテストが仕込まれていてエラー起こしたのでその対策
        if not s:
            return 0
        
        #ディクショナリを作る
        dic1= {}    #カウンター
        dic2= {}    #最長記録保管

        #文字を一文字づつ見ていく
        for moji1 in s:
            #print(moji1)
            
            #新規の文字ならカウンターを作成
            if moji1 not in dic1:
                dic1[moji1]=0
                
            #既存の文字なら自己カウンターを記録してリセット
            else:
                num_s=dic1[moji1]
                #過去記録と比較して短いなら上書き保存の必要はない
                try:
                    if dic1[moji1] < dic2[moji1]:
                        pass
                    else:
                        dic2[moji1]=dic1[moji1]                    
                except:
                    dic2[moji1]=dic1[moji1]
                    
                dic1[moji1]=0

                #先の重複カウンターよりも長いすべてのカウンターを記録して削除
                for key2 in list(dic1.keys()):#for文の中で参照中のコンテナの要素は削除できないのでコピーリストを作って回す
                    if dic1[key2] > num_s:
                        
                        #過去記録と比較して短いなら上書き保存の必要はない
                        try:
                            if dic1[key2] < dic2[key2]:
                                pass
                            else:
                                dic2[key2]=dic1[key2]
                        except:
                            dic2[key2]=dic1[key2]

                        del dic1[key2]
            
            #すべての文字のカウンターを＋１
            for key1,num1 in dic1.items():
                dic1[key1] = num1+1

        #過去記録と比較して短いなら上書き保存の必要はない
        for key3 in dic1:
            try:
                if dic1[key3] < dic2[key3]:
                    pass
                else:
                    dic2[key3]=dic1[key3]                    
            except:
                dic2[key3]=dic1[key3]
        
        print(dic1,dic2)
        return max(dic2.values())


#test入力

hoge=Solution()
print(f"outoput={hoge.lengthOfLongestSubstring("abcabcbb")}")
