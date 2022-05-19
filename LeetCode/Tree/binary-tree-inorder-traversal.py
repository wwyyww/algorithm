#94. Binary Tree Inorder Traversal
#문제 링크 : https://leetcode.com/problems/binary-tree-inorder-traversal/

#내 풀이
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        output=[]
        
        if not root:
            return root
        
        def inorder(root):
            
            if root:
                inorder(root.left)
                output.append(root.val)
                inorder(root.right)

        
            
        inorder(root)
        
        return output
                