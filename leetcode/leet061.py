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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        node1 = head
        node3 = head
        node5 = head
        count1 = 0
        count2 = 0
        
        #長さ1未満の場合
        if head is None or node5.next is None:
            return head

        #リスト長を確認して、回転数をリスト長以内に割る
        while True:
            node6 = node5.next
            node5 = node6
            count1 += 1
            if node6.next is None:
                break

        count1 += 1
        k %= count1
        print(k,count1)

        #回転の必要がない場合    
        if k == 0:
            return head

        #新先頭を保存し、末尾までいく
        while True:
            node2 = node1.next
            node1 = node2
            count2 += 1
            if count2 == count1-k:
                node_newhead = node2
            if node2.next is None:
                break
    
        #新末尾で切る
        if k == count1-1:
            head.next = None
        else:
            for i in range(count1-k-1):
                node4 = node3.next
                node3 = node4
            else:
                node4.next = None
        
        #切った「先頭〜新末尾」を「新先頭〜末尾」の後ろにくっつける
        node2.next = head

        return node_newhead


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
#linked_list = create_linked_list([1,2,3,4,5,6,7,8,9,0])
linked_list = create_linked_list([0,1,2])
print(f"入力リスト: {print_linked_list(linked_list)}")

hoge=Solution()
print(print_linked_list(hoge.rotateRight(linked_list,3)))

"""
単方向連結リストのローテート
入力kの分だけリストをずらす
1:10
"""