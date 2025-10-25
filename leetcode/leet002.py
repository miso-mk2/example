#「空でない一桁非負整数リストノード」ｘ２が入力される
#これを両リスト共、逆順でstr連結して要素数桁の整数にして、
#二つのリストからできた整数を足し合わせた合計を、
#また逆順で桁ごとにバラしてリストノードで出力する

#普通のリストではなく、「連結リスト」
#要素をノードとして、値だけでなく繋がりの情報（ポインタ）を保有するリスト
#pythonに組み込まれている機能ではないので↓のクラス作成が必要

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #一旦全部リストから取り出して文字列に変換する（逆順で結合）
        str1=""
        str2=""
        while l1 is not None:   #リストが空になったら終了
            str1 = str(l1.val) + str1
            # 次のノードへ移動
            l1 = l1.next
        while l2 is not None:   #リストが空になったら終了
            str2 = str(l2.val) + str2
            # 次のノードへ移動
            l2 = l2.next

        #出来上がった数値を計算
        print(str1,str2)
        str_sum = str(int(str1)+int(str2))

        #サイド連結リストを作成
        #先頭に空のダミーを置いておくと操作しやすい
        dummy = ListNode(0)
        now_node = dummy

        for i in str_sum[::-1]:
            new_node = ListNode(int(i))
            now_node.next = new_node
            now_node = new_node

        #ダミーの次のノードを指定して出力
        return dummy.next

#test用に連結リストを作成して入力する場所

def renketu_list_input3(num1,num2,num3):
    node1=ListNode(num1)
    node2=ListNode(num2,next=node1)
    node3=ListNode(num3,next=node2)
    return node3

hoge = Solution()
l1= renketu_list_input3(3,4,2)
l2= renketu_list_input3(5,6,4)
print(hoge.addTwoNumbers(l1,l2))

