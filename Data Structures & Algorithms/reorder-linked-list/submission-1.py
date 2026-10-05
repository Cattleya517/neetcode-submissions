# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def split(p):
            #截斷前半並返回後半
            s, f = p, p.next
            while f and f.next:
                s = s.next
                f = f.next.next
            latter = s.next
            s.next = None
            return latter
              
        def reverse(p):
            prev, curr = None, p
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        former = head
        latter = reverse(split(head))

        while latter:
            former_next = former.next
            latter_next = latter.next

            former.next = latter
            latter.next = former_next
            former = former_next
            latter = latter_next
            
