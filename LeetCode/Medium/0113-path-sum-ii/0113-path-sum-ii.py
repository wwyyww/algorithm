# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        paths = []

        def dfs(node, total, path):
            total += path[-1]
            if not node.left and not node.right:
                if total == targetSum:
                    paths.append(path)
                    return
            if node.left:
                dfs(node.left, total, path+[node.left.val])
            if node.right:
                dfs(node.right, total, path+[node.right.val])
        if root:
            dfs(root, 0, [root.val])
        return paths