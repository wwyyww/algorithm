# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        output = False
        def dfs(node, total: int):
            nonlocal output
            if not node.left and not node.right:
                if total == targetSum:
                    output = True
                    return
            
            if node.left:
                dfs(node.left, total+node.left.val)
            if node.right:
                dfs(node.right, total+node.right.val)
        if root:
            dfs(root, root.val)

        return output
        