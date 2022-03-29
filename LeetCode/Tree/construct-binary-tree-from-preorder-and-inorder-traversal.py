#105. Construct Binary Tree from Preorder and Inorder Traversal
#문제 링크 : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#실패
#책 풀이

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node

'''
트리를 순회하는 방법에는 전위, 중위, 후위 순회가 있는데 이 중 2가지만 있어도 이진 트리를 복원할 수 있다. 
전위순회는 루트 → 좌 → 우 이고 중위 순회는 좌 → 루트 → 우 순이다.

우선 전위순회를 통해 루트노드의 값은 알 수 있다. 
알아낸 루트 값은 중위 순회에서 좌, 우를 나누는 기준으로 사용할 수 있다. 
이 방식으로 계손 분할을 해나가면 트리를 구성할 수 있다.
'''