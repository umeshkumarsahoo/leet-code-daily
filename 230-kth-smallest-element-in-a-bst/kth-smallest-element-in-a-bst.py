class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)   
            val.append(node.val)
            inorder(node.right)  

        inorder(root)            
        
        return val[k-1]         