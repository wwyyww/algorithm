#2178. 미로 탐색
#문제 링크 : https://www.acmicpc.net/problem/2178

#내 풀이
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze=[[0] for _ in range(n+1)]
visited=[[False]*(m+1) for _ in range(n+1)]


for i in range(n):
    nums=list(sys.stdin.readline().strip())
    for num in nums:
        maze[i+1].append(int(num))

q=deque()
q.append((1,1))
visited[1][1]=True

while q:
    now=q.popleft()
    x=now[0]
    y=now[1]
    if x==n and y==m:
        break

    if y-1>0:
        if maze[x][y-1]==1 and not visited[x][y-1]:
            visited[x][y-1]=True
            maze[x][y-1]=maze[x][y]+1
            q.append((x, y-1))
    if y+1<=m:
        if maze[x][y+1]==1 and not visited[x][y+1]:
            visited[x][y+1]=True
            maze[x][y+1]=maze[x][y]+1
            q.append((x, y+1))
    if x-1>0:
        if maze[x-1][y]==1 and not visited[x-1][y]:
            visited[x-1][y]=True
            maze[x-1][y]=maze[x][y]+1
            q.append((x-1, y))
    if x+1<=n:
        if maze[x+1][y]==1 and not visited[x+1][y]:
            visited[x+1][y]=True
            maze[x+1][y]=maze[x][y]+1
            q.append((x+1, y))

print(maze[n][m])


'''
나는 조건식을 하나하나 했는데 책에서는
[0, 1, 0, -1] 이렇게 리스트를 만들어서 반복문을 사용했다.
내가 이 문제에서의 x, y 기준이 헷갈려서 범위 판단을 할 때 잘못했었다.
bfs는 구현하겠는데 최소 칸 수는 어떻게 구해야 할지 모르겠어서
책을 참고해 값에 +1씩 추가하는 부분을 추가했다.
'''