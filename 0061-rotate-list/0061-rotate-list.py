# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        if not head or not head.next or k==0:
            return head
        length=1
        tail=head
        while tail.next:
            length+=1
            tail=tail.next
        tail.next=head
        k%=length
        if k==0:
            tail.next=None
            return head
        to_move=length-k
        new=head
        for _ in range(to_move-1):
            new=new.next
        new_head=new.next
        new.next=None
        return new_head






        