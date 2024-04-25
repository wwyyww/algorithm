#1987. 알파벳
#문제 링크 : https://www.acmicpc.net/problem/1987

#내 풀이 - python으로 실행하면 시간초과뜨고 pypy3로 실행해야 통과함
import sys

r, c = map(int, sys.stdin.readline().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))

def dfs(sx, sy, visited):
    start_ascii_code = ord(graph[sx][sy]) - 65
    global squares
    squares = max(squares, visited[start_ascii_code])

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if (0 <= nx < r) and (0 <= ny < c):
            ascii_code = ord(graph[nx][ny]) - 65
            if not visited[ascii_code]:
                visited[ascii_code] = visited[start_ascii_code] + 1
                dfs(nx, ny, visited)
                visited[ascii_code] = 0

squares = 0
visited = [0]*26
start_ascii_code = ord(graph[0][0]) - 65
visited[start_ascii_code] = 1
dfs(0, 0, visited)
print(squares)


#다른 풀이 : https://leeingyun96.tistory.com/22 참고

import sys

r, c = map(int, sys.stdin.readline().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))

def dfs(sx, sy):
    q = set()
    q.add((sx, sx, graph[sx][sy]))
    squares = 0

    while q:
        x, y, now_visited = q.pop()

        squares = max(squares, len(now_visited))
        if squares == 26:
            return 26

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] not in now_visited:
                q.add((nx, ny, now_visited + graph[nx][ny]))

    return squares

print(dfs(0, 0))

'''
이 코드는 파이썬으로 통과한다. 내 코드랑 비교해서 시간이 7배나 빨라진다.
'''