from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        result=[]
        if not root:
            return result
        queue.append(root)
        while len(queue)>0:
            level=len(queue)
            for i in range(len(queue)):
                curr=queue.popleft()
                if i==level-1:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result
                
        

        