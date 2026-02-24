# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=[]
        def preorder(node,string):
            if not node:
                return
            if not node.left and not node.right:
                res.append(string+str(node.val))
                return
            preorder(node.left,string+str(node.val))
            preorder(node.right,string+str(node.val))
        preorder(root,"")
        total=0
        for num in res:
            total+=int(num,2)
        return total