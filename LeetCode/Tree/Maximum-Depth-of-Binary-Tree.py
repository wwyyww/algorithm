#104. Maximum Depth of Binary Tree
#문제 링크 : https://leetcode.com/problems/maximum-depth-of-binary-tree/

#책 풀이

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth

'''
DFS는 스택을 사용하고 BFS는 큐를 사용해서 구현한다.

앞에 그래프 챕터에서 DFS로 풀이할 때는 항상 재귀구조를 사용해서 풀었는데 BFS는 반복구조로 풀 수 있다.

deque를 사용해서 큐를 정의한다. 리스트로도 큐 연산을 할 수 있지만 데크를 사용하면 양방향 추출을 O(1)에 추출할 수 있다. 

queue에서 노드를 하나씩 pop해서 자식노드가 있는지 확인하고 자식노드가 있으면 큐에 추가한다. 
for문에서 부모 노드의 좌, 우 자식 노드를 모두 확인하기 때문에 while이 실행될 때마다 depth에 1을 더하면 된다.

나는 풀려고 할 때 깊이를 계산하는 시점을 잘못 생각했다. 그리고 나도 while문을 사용했는데
반복문을 나가지를 못했다. 근데 당연히 pop을 추가하는 것보다 적게 하니까 계속 반복될 수 밖에 없었다.
'''