# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes=[]
        if not root:
            return None
        def preorder(node):
            if not node:
                return 
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        for n in range(len(nodes)-1):
            nodes[n].left=None
            nodes[n].right=nodes[n+1]
        nodes[-1].left=None
        nodes[-1].right=None
    