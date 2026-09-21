# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        s, f = dummy, head
        for i in range(n):
            f = f.next
        while f:
            s = s.next
            f = f.next
        # 移除目標node (s.next)
        s.next = s.next.next

        return dummy.next

        