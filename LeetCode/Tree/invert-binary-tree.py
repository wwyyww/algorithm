#226. Invert Binary Tree
#문제 링크 : https://leetcode.com/problems/invert-binary-tree/

#책 풀이 : BFS
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

'''
문제가 하라는대로 좌우를 바꾸고 계속 다음노드를 추가해서 바꾸면 된다.
이 문제를 풀 때 반환을 어떻게 해야될지를 몰랐는데 그냥 root를 반환하면 되는거였다.
'''