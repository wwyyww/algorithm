#310. Minimum Height Trees
#문제 링크 : https://leetcode.com/problems/minimum-height-trees/
#실패
#책 풀이 : 단계별 리프 노드 제거

import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

'''
리프 노드(최하위 노드)를 하나씩 제거해서 남아있는 값을 찾으면 그 값이 최소 높이를 만들 수 있는 노드가 된다. 
딕셔너리를 활용해서 그래프를 구성한다. 리프노드를 leaves에 추가한다. 
리프노드는 graph 딕셔너리에서 해당 키의 값이 1개인 키를 찾으면 된다.

그래프에서 리프노드를 pop으로 제거하고 해당 노드와 연결된 값도 제거한다. 
무방향그래프라서 노드끼리 두번 연결해주었기 때문에 두번 제거해야 한다. 
제거한 후 그래프에서 값이 1개인 노드는 new_leaves에 넣어서 제거를 반복한다.
'''