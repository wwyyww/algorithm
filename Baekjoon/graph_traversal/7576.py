#7576. 토마토
#문제 링크 : https://www.acmicpc.net/problem/7576

#내 풀이
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    tomato = list(map(int, sys.stdin.readline().split()))
    graph.append(tomato)

def bfs(point_list):
    q = deque([])
    for point in point_list:
        q.append(point)

    while q:
        y, x = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append([ny, nx])

#bfs를 호출할 때 값이 1인 좌표들을 모두 전달
points = []
for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == 1:
            points.append([i, j])

if len(points) == m*n:
    print(0)
    exit()
elif len(points) == 0:
    print(-1)
    exit()
else:
    bfs(points)

day = 0
for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        else:
            day = max(graph[i][j], day)

print(day - 1)