#11725. 트리의 부모 찾기
#문제 링크 : https://www.acmicpc.net/problem/11725

#내 풀이

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = [1] * (n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque([1])
    visited[1] = 1

    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)
                answer[node] = now

bfs()

for i in range(2, n+1):
    print(answer[i])