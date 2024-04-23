#14502. 연구소
#문제 링크 : https://www.acmicpc.net/problem/14502

#내 풀이

import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(vx, vy):
    q = deque([])
    q.append([vx, vy])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) :
                if ((tmp_graph[nx][ny] == 0) or (tmp_graph[nx][ny] == 2)) and not visited[nx][ny]:
                    tmp_graph[nx][ny] = 2
                    visited[nx][ny] = 1
                    q.append([nx, ny])

def check_area(tmp_graph):
    area = 0        
    for j in range(n):
        for k in range(m):
            if tmp_graph[j][k] == 0:
                area += 1
    return area
    

visited = [[0] * m for _ in range(n)]
points = []
virus_points = []

# 0인 좌표, 2인 좌표들 찾기
for j in range(n):
    for k in range(m):
        if graph[j][k] == 0:
            points.append([j, k])
        elif graph[j][k] == 2:
            virus_points.append([j, k])

search_points = list(combinations(points, 3))
areas = []

for sp in search_points:
    tmp_graph = copy.deepcopy(graph)

    for p in sp:
        sx, sy = p
        tmp_graph[sx][sy] = 1
    visited = [[0] * m for _ in range(n)]
    for vp in virus_points:
        vx, vy = vp
        if not visited[vx][vy]:
            bfs(vx, vy) 
    area = check_area(tmp_graph)
    areas.append(area)

print(max(areas))
