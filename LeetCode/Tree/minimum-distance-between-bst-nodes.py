#783. Minimum Distance Between BST Nodes
#문제 링크 : https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#실패
#책 풀이 : 재귀 구조로 중위 순회

import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

'''
내가 시도했던 풀이로 틀린 이유는 내가 부모, 자식 노드 사이의 차이로만 비교했기 때문이다.

하나의 부모 노드와 차이가 가장 작을 수 있는 노드는 왼쪽 자식에서 가장 오른쪽에 있는 노드와 
오른쪽 노드에서 가장 왼쪽에 있는 노드다. 
탐색 순서를 왼쪽 자식 → 부모노드 → 오른쪽 자식과 비교하기 때문에 중위 순회를 하면 된다. 

prev는 이전에 탐색한 노드의 값이고 해당 값과 현재 값을 비교한다. 
만약 주어진 트리가  `[4,2,6,1,3]`  이라면 탐색 순서는 다음과 같다. 
1, 2 비교 → 2, 3 비교 → 3, 4 비교 → 4, 6 비교

prev의 초기값은 -sys.maxsize로 해야 처음 탐색할 때 
result의 값이 최대값으로 유지되기 때문에 -sys.maxsize다.
'''