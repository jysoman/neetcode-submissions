# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        level = 0
        res = []
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    # temp.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    # temp.append(curr.right.val)
            res.append(temp)
            level+=1
            
        return res
