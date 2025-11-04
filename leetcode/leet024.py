# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    
    # 最初のノード（リストの先頭）を作成
    head = ListNode(values[0])
    current = head
    
    # 2番目以降のノードを作成し、current の next に繋ぐ
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next # ポインタを新しいノードに移動

    return head

#_________________________________________________

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #「一個前」「奇数」「偶数」をそれぞれ記録
        nodeZ = None
        nodeA = head

        #要素がないなら返してしまう
        if head is None:
            return head
        #要素が一個しかないなら返してしまう
        if head.next is not None:
            nodeB = head.next
        else:
            return head

        #ループ処理
        while True:

            if nodeZ is not None:
                nodeZ.next = nodeB
                #print("頭でない")
            else:
                head = nodeB
            
            if nodeA.next.next is not None:
                nodeA.next = nodeA.next.next
                #print("末尾でない")
            else:
                nodeA.next = None
                nodeB.next = nodeA
                return head
            
            nodeB.next = nodeA

            if nodeA.next.next is not None:
                #print("もう一周ある")
                nodeZ=nodeA
                nodeB=nodeA.next.next
                nodeA=nodeA.next
            else:
                return head
            
            #print(f"nodeZ={nodeZ.val}")
            #print(f"nodeA={nodeA.val}")
            #print(f"nodeB={nodeB.val}")

#_________________________________________________

# 【テスト用のヘルパー関数】リストの内容を表示する関数（確認用）
def print_linked_list(head: Optional[ListNode]):
    values = []
    current = head
    
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)

# リストを作成
linked_list = create_linked_list([1,2,3,4,5,6,7])
print(f"入力リスト: {print_linked_list(linked_list)}")

hoge = Solution()
result_head = hoge.swapPairs(linked_list)

# 結果のリストを表示 (デバッグ用)
print(f"出力リスト: {print_linked_list(result_head)}")

"""
連結リストの要素を２個づつ入れ替えていく

"""