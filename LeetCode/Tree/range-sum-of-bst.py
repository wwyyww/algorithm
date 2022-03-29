#938. Range Sum of BST
#문제 링크 : https://leetcode.com/problems/range-sum-of-bst/

#내 풀이
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    output:int=0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        
        q=deque([root])
        
        while q:
            node=q.popleft()
            if not node:
                continue
                
            if node.val<=high and node.val>=low:
                self.output+=node.val
                
            q.append(node.left)
            q.append(node.right)
        
        return self.output

'''
그냥 노드들 다 비교해서 범위 확인하고 더했다.
'''

#책 풀이 : 반복구조 DFS

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum

'''
나와 비슷한 풀이에서 q가 아닌 스택을 사용했고 스택에 추가할 때 범위를 확인하고 넣는 방식으로 진행했다. 
확실히 범위를 확인하고 넣으니까 시간이 조금 덜 걸린다.
'''