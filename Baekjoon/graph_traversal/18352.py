#18352. 특정 거리의 도시 찾기
#문제 링크 : https://www.acmicpc.net/problem/18352

#내 풀이

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
search=deque()
search.append(x)
visited=[False]*(n+1)
dist=[0]*(n+1)
output=[]


#그래프 생성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited[x]=True

while search:
    start=search.popleft()
    
    for node in graph[start]:
        if not visited[node]:
            visited[node]=True
            dist[node]=dist[start]+1
            search.append(node)

for i in range(1, n+1):
    if dist[i]==k:
        output.append(i)

if output:
    print(*output, sep='\n')
else:
    print(-1)

'''
그래프를 생성하고 방문 여부 체크 리스트와 거리를 계산하기 위한 리스트를 만들었다.
BFS 탐색을 진행하기 위해 큐를 사용했다. while문으로 방문여부를 체크하고 
인접노드를 추가하고 거리 계산을 했다.
'''