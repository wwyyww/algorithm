#1753. 최단경로
#문제 링크 : https://www.acmicpc.net/problem/1753

#내 풀이 - 틀림
import sys
from collections import deque

v, e=map(int, sys.stdin.readline().split())
start=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

visited=[False]*(v+1)
dist=[sys.maxsize]*(v+1)
dist[start]=0
visited[start]=True

queue=deque()
queue.append(start)

while queue:
    now=queue.popleft()
    for node in graph[now]:
        dist[node[0]]=min(dist[now]+node[1], dist[node[0]])
        if not visited[node[0]]:
            visited[node[0]]=True
            queue.append(node[0])

for i in range(1, v+1):
    if dist[i]==sys.maxsize:
        print("INF")
    else:
        print(dist[i])


#책 풀이

import sys
import heapq

v, e=map(int, sys.stdin.readline().split())
start=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

visited=[False]*(v+1)
dist=[sys.maxsize]*(v+1)
dist[start]=0

heap=[]
heapq.heappush(heap, (dist[start], start))
visited[start]=True

while heap:
    now=heapq.heappop(heap)
    now_dist=now[0]
    now_node=now[1]
    for node in graph[now_node]:
        if dist[now_node]+node[1]<dist[node[0]]:
            dist[node[0]]=dist[now_node]+node[1]
            heapq.heappush(heap, (dist[node[0]],node[0]))
            if not visited[now_node]:
                visited[now_node]=True

for i in range(1, v+1):
    if dist[i]==sys.maxsize:
        print("INF")
    else:
        print(dist[i])

'''
<내 풀이와 책 풀이의 다른 점>
1. 우선 내 풀이는 우선순위 큐를 사용하지 않았다.
- 큐에서 pop을 할 때 가중치가 제일 작은 노드를 pop해야 한다.
2. 가중치가 업데이트 되는 경우에만 큐에 값을 넣어야 하는데 방문만 안 했다면 무조건 추가했다. 

'''