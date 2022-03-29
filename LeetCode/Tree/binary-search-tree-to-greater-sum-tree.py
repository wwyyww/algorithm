#1038. Binary Search Tree to Greater Sum Tree
#문제 링크 : https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
#실패
#책 풀이 : 중위 순회

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root

'''
중위순회 : 오른쪽 → 루트 → 왼쪽 순으로 진행
self.val이 누적값이다. 함수는 입력받은 노드의 가장 오른쪽 노드부터 즉 가장 큰 값부터 더하기 시작한다. 
오른쪽 값을 더한 후에는 왼쪽 값을 함수의 인자로 넣어준다. 
그렇게 오른쪽 → 루트 → 왼쪽 순으로 노드 값이 누적된다. 최종 출력을 위해서 root를 반환한다.
'''