#100. Same Tree
#문제 링크 : https://leetcode.com/problems/same-tree/

#내 풀이
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return True
        
        p_queue=deque([p])
        q_queue=deque([q])
        
        while p_queue and q_queue:
            
            for _ in range(len(p_queue)):
                cur_p=p_queue.popleft()
                cur_q=q_queue.popleft()
                
                if cur_p and cur_q:
                    if cur_p.val==cur_q.val:
                        p_queue.append(cur_p.left)
                        p_queue.append(cur_p.right)
                        q_queue.append(cur_q.left)
                        q_queue.append(cur_q.right)
                    else:
                        return False
                if (cur_p and not cur_q) or (not cur_p and cur_q):
                    return False

        return True

'''
두 트리가 같은 트리인지 확인하는 문제다.
deque를 사용해서 풀었다.
현재 두 노드 모두 null이 아니면 값이 같은지 확인한다.
만약 둘중에 하나는 값이 있고 하나는 값이 없으면 False를 반환한다.
해당 while문을 잘 빠져나오면 같은 트리라고 판단한다.
'''