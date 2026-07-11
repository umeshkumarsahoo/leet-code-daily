# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        else: 
            return None
        pointer1=head
        pointer2=slow
        while pointer1!=pointer2:
            pointer1=pointer1.next
            pointer2=pointer2.next
        return pointer1