#111. Minimum Depth of Binary Tree
#문제 링크 : https://leetcode.com/problems/minimum-depth-of-binary-tree/

#내 풀이
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        
        q=deque([root])
        depth=0
        
        
        while q:
            depth+=1
            
            for _ in range(len(q)):
                cur_root=q.popleft()
                if not cur_root.left and not cur_root.right:
                    return depth
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
        
'''
큐를 사용해서 구현했다. 만약 자식 노드가 둘 다 없으면 그때의 깊이를 반환한다.
'''