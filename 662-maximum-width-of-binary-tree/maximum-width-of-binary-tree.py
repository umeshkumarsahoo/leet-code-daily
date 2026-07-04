# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([(root,0)])
        max_width=float('-inf')
        while q:
            lvl_length=len(q)
            for i in range(lvl_length):
                node,curr=q.popleft()
                if i==0: first=curr
                if node.left:
                    q.append([node.left,2*curr])
                if node.right:
                    q.append([node.right,2*curr+1])
            max_width=max(curr-first+1,max_width)
        return max_width




        