#1260. DFS와 BFS
#문제 링크 : https://www.acmicpc.net/problem/1260

#내 풀이
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
nums=[[] for _ in range(n+1)]
visited=[False]*(n+1)
dfs_output=""
bfs=""
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    nums[a].append(b)
    nums[b].append(a)

def dfs(num):
    global dfs_output
    visited[num]=True
    dfs_output+=str(num)+" "

    for node in sorted(nums[num]):
        if not visited[node]:
            dfs(node)
    
dfs(v)

visited=[False]*(n+1)
q=deque()
q.append(v)
visited[v]=True

while q:
    num=q.popleft()
    bfs+=str(num)+" "
    for node in sorted(nums[num]):
        if not visited[node]:
            visited[node]=True
            q.append(node)
    
print(dfs_output)
print(bfs)

'''
문제에서 정점이 여러개면 정점 번호가 작은 것부터 방문하는 조건을 나중에 봤다.
문제를 잘 읽자.
BFS는 재귀함수로 구현하지 못하고 큐를 사용해야 한다.
'''