class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        #数字ごとのカウンター
        lst1=[]

        #3方向のチェック
        for i0 in range(3):
            #print(f"i0={i0}")

            #縦横
            for i1 in range(9):
                #print(f"i1={i1}")

                for i2 in range(9):

                    #カウンターで１〜９を確認
                    for i3 in range(9):
                        
                        #初回だけカウンター作成
                        if i1 == 0 and i2 ==0:
                            lst1.append(0)
                        
                        #箱探索用のインデックス計算
                        if i0==0:
                            index1 = i1
                            index2 = i2
                        elif i0==1:
                            index1 = i2
                            index2 = i1
                        elif i0==2:
                            index1 = i2%3 + i1%3*3
                            index2 = i2//3 + i1//3*3

                        #探索してカウンターを加算
                        if str(i3+1) == board[index1][index2]:
                            lst1[i3] += 1


                #2個以上の数字があるかどうかの判定
                if any(item >= 2 for item in lst1):
                    return False
                    #print("ある")
                else:
                    pass
                    #print("ない")
                    
                #lst1をリセット
                lst1[:]=[0]*len(lst1)

        return True

hoge=Solution()
huga=[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
print(hoge.isValidSudoku(huga))

"""
数独のダブりを確認
数独盤として二重配列が渡される
問題として解けるかどうかは気にしなくて良い模様
"""