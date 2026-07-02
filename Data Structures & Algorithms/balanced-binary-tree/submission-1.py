class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
    
    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))