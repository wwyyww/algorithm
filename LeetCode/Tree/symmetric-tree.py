#101. Symmetric Tree
#문제 링크 : https://leetcode.com/problems/symmetric-tree/

#풀이

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        
        left=root.left
        right=root.right
        
        left_q=deque([left])
        right_q=deque([right])
        
        while left_q and right_q:
            
            left_node=left_q.popleft()
            right_node=right_q.popleft()
            
            if left_node and right_node:
                if left_node.val!=right_node.val:
                    return False

                left_q.append(left_node.right)
                left_q.append(left_node.left)
                right_q.append(right_node.left)
                right_q.append(right_node.right)
                
            elif left_node or right_node:
                return False
            
        return True
        
    

'''
풀이 참고 : https://leetcode.com/problems/symmetric-tree/discuss/2245628/Recursive-and-Interative-Solutions-in-Python3.-Easy-to-understand
다른 사람의 풀이를 참고했다. 보통은 재귀함수를 사용해서 많이 풀었는데 반복문으로 풀고 싶어서 풀이를 찾아보았다.
처음 루트 노드에서 왼쪽, 오른쪽을 아예 나눠서 시작한다.
각 노드의 값, 값의 유무를 조건으로 확인해서 대칭 구조인지 확인하는 방식이다.

'''