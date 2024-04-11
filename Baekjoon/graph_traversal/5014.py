#5014. 스타트링크
#문제 링크 : https://www.acmicpc.net/problem/5014

#내 풀이

import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

def bfs(x):
    q = deque([x])
    visited[x] = 1

    while q:
        now = q.popleft()
        if now == G :
            return True
        else:
            nu = now + U
            nd = now - D
            if 0 < nu <= F and visited[nu] == 0:
                q.append(nu)
                visited[nu] = visited[now] + 1
            if 0 < nd <= F and visited[nd] == 0:
                q.append(nd)
                visited[nd] = visited[now] + 1

is_find = False
visited = [0 for _ in range(F+1)]
is_find = bfs(S)

if is_find:
    print(visited[G]-1)
else:
    print("use the stairs")