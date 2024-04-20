#1926. 그림
#문제 링크 : https://www.acmicpc.net/problem/1926

#내 풀이
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []

for _ in range(n):
    paints = list(map(int, sys.stdin.readline().split()))
    graph.append(paints)

def bfs(sy, sx):
    
    q = deque([])
    q.append([sy, sx])
    visited[sy][sx] = True
    cnt = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = 1
                cnt += 1
    return cnt

results = []
visited = [[0]*m for _ in range(n)]

for j in range(0, n):
    for k in range(0, m):
        if graph[j][k] == 1 and visited[j][k] == 0:
            cnt = bfs(j, k)
            results.append(cnt)

print(len(results))
if len(results) == 0:
    print(0)
else:
    print(max(results))