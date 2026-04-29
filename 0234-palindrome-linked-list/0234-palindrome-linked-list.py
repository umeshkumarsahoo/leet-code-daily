# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        near,far=0,len(arr)-1
        while near<=far:
            if arr[near]!=arr[far]:
                return False
                break
            near+=1
            far-=1 
        return True

