# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        maxi=float('-inf')
        n=len(arr)
        for i in range(n//2):
            maxi=max(maxi,arr[i]+arr[n-i-1])
        return maxi
            
            