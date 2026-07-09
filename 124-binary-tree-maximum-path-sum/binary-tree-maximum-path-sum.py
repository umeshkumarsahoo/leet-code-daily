# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            nonlocal maxi
            if not node: return 0
            left,right=max(solve(node.left),0),max(solve(node.right),0)
            apne_chote_bachhe=left+right+node.val
            maxi=max(maxi,apne_chote_bachhe)
            return max(left,right)+node.val
        maxi=float('-inf')
        solve(root)
        return maxi


        