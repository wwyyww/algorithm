#10026. 적록색약
#문제 링크 : https://www.acmicpc.net/problem/10026

#내 풀이

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))

def bfs(sx, sy, color_blindness):
    q = deque([])
    q.append([sx, sy])
    color = graph[sx][sy]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) :
                if color_blindness:
                    if not visited_blind[nx][ny]:
                        if (graph[nx][ny] in 'RG' and color in 'RG') or graph[nx][ny] == color:
                            visited_blind[nx][ny] = 1
                            q.append([nx, ny])
                else:
                    if graph[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append([nx, ny])

visited_blind = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

color_blind_zones = 0
color_zones = 0

for j in range(n):
    for k in range(n):
        if not visited_blind[j][k]:
            visited_blind[j][k] = 1
            bfs(j, k, 1)
            color_blind_zones += 1
        if not visited[j][k]:
            visited[j][k] = 1
            bfs(j, k, 0)
            color_zones += 1

print(color_zones, color_blind_zones)
