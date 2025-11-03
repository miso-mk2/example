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
#__________________________________________


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #print(head.val)
        #print(head.next.val)

        #要素数が１個しかない場合は削除してリターン
        if head.next is None and n == 1:
            return None # 新しいリストの先頭は None になる

        #頭から要素数を数える
        node1 = head
        size=0
        while node1 is not None:
            size+=1
            node1 = node1.next
        print(f"要素数={size}")

        #ヘッドの削除を求められている場合
        if size==n:
            head = head.next
        
        #頭から「指定ノード一個前」のノードを取得
        node2 = head
        for i in range(size-n-1):
            node2 = node2.next

        #頭から「指定ノード一個後」のノードを取得
        node3 = head
        for i in range(size-n+1):
            node3 = node3.next

        #一個前ノードのnextを一個後ノードに書き換えて、
        #指定ノードがリストから削除される
        node2.next = node3

        return head



#__________________________________________

"""
# 【テスト用のヘルパー関数】リストの内容を表示する関数（確認用）
def print_linked_list(head: Optional[ListNode]):
    values = []
    current = head
    
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)
"""
# リストを作成
#linked_list = create_linked_list([1, 2, 3, 4, 5])
linked_list = create_linked_list([1])
#print(f"作成されたリスト: {print_linked_list(linked_list)}")

hoge = Solution()
result_head = hoge.removeNthFromEnd(linked_list, 2)

# 結果のリストを表示 (デバッグ用)
#print(f"removeNthFromEndの結果: {print_linked_list(result_head)}")

"""
入力の連結リストの、「後ろからn番目のノード」を削除して。連結リストを返す

"""