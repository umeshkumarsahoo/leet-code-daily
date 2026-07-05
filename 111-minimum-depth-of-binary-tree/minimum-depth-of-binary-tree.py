# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_dist=float('inf')
        def dfs(node,curr_depth):
            nonlocal min_dist
            if not node: return
            if not node.left and not node.right:
                min_dist=min(curr_depth,min_dist)                
                return 
            dfs(node.left,curr_depth+1)
            dfs(node.right,curr_depth+1)
        dfs(root,1)
        return min_dist

            
        