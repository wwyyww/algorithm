#11403. 경로 찾기
#문제 링크 : https://www.acmicpc.net/problem/11403

#내 풀이

import sys
from collections import deque

def bfs(node):
    q = deque([node])
    
    while q:
        now = q.popleft()
        if graph[now]:
            for g in graph[now]:
                if not visited[node][g]:
                    visited[node][g] = 1
                    q.append(g)

n = int(sys.stdin.readline())
graph = [[] for i in range(n)]

for i in range(n):
    nodes = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if nodes[j] == 1:
            graph[i].append(j)

visited = [[0]*n for i in range(n)]

for i in range(n):
    bfs(i)

for i in range(n):
    print(*visited[i])
