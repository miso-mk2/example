class Solution:
    def simplifyPath(self, path: str) -> str:
        #print(path)

        output = []
        len_path = len(path)

        str1 = ""
        str2 = ""

        for i in range(len_path):
            #print(f"i={i}")

            #終了条件を満たすならstr1を切断してstr2を作る
            #そうでないならstr1を伸ばしていく

            #末尾でなく文字数がありスラッシュなら切断
            if i < len_path-1 and len(str1) > 1 and path[i] == "/":
                #末尾でなく、スラッシュで、次もスラッシュならスキップ
                if path[i+1] =="/":
                    continue
                str2 = str1
                str1 = "/"
            #末尾なら（スラッシュは除去しつつ）切断
            elif i == len_path-1:
                if len(str1)==0 or not path[i] == "/":
                    str1 += path[i]
                str2 = str1
            
            else:
                str1 += path[i]
                continue

            #切断して作ったstr2の精査
            if str2 == "/..":
                if len(output) > 0:
                    output.pop()
                continue
            elif str2 == "/.":
                continue
            elif str2 == "//":
                continue
            else:
                output.append(str2)
        
        if len(output) == 0:
            return "/"
        return "".join(output)

hoge = Solution()
print(hoge.simplifyPath("///"))
#print(hoge.simplifyPath("/1/2/3//.."))

"""
unix形式のファイルパスを正規パスに変換する
スラッシュやピリオドを正しい形に処理する
1:36
"""

"""

完全にルールに反するようなパスは来ないのか？不明
条件をまとめる
・スラッシュが連続するなら何個でも1個にする
・末尾のスラッシュは消す（ルートディレクトリの場合は例外としてスラッシュ単体を認める）

・ピリオドは、文字列に含む場合は連続2個以下の場合有効と認めない 3個以上なら有効
・2個以下のピリオドは、文字を含まない単体なら相対ディレクトリとして認め、必要な分ディレクトリをずらす
・ピリオド2個でずらす場合、ルートから上には行けない

"""