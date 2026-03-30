# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_d = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        temp = head
        while temp:
            if temp.val in to_d:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return dummy.next