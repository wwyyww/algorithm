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
        curr = None
        def preorder(node):
            if node is None:
                return
            nonlocal curr
            left, right = node.left, node.right
            node.left = None
            if curr:
                curr.right = node
                curr = curr.right

            else:
                curr = node

            preorder(left)
            preorder(right)

        preorder(root)