class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque([root])

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                curr.left, curr.right = curr.right, curr.left

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root