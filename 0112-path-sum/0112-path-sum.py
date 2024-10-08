# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        return self.path_find(root,targetSum)
    def path_find(self,root,targetSum)->bool:
        if not root: return False
        if not root.left and not root.right: return root.val==targetSum
        targetSum-=root.val
        return self.path_find(root.left,targetSum) or self.path_find(root.right,targetSum)
        