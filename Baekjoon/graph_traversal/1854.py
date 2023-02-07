#1854. K번째 최단경로 찾기
#문제 링크 : https://www.acmicpc.net/problem/1854

#내 풀이 - 실패(메모리초과)

import sys
from collections import deque

n, m, k=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start=1
q=deque()
q.append(start)

dist=[[] for _ in range(n+1)]
visited=[False]*(n+1)

while q:
    now=q.popleft()
    if visited[now]:
        continue
    visited[now]=True
    for node in graph[now]:
        nxt_node=node[0]
        nxt_dist=node[1]
        if len(dist[nxt_node])==0:
            dist[nxt_node].append(nxt_dist)            
        tmp=[i+nxt_dist for i in dist[now]]
        dist[nxt_node]+=tmp
        q.append(nxt_node)


for d in dist[1:]:
    if len(d)<k:
        print(-1)
    else:
        d=list(set(d))
        d.sort()
        print(d[k-1])


#책 풀이

import sys
import heapq

n, m, k=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start=1
q=[(0,1)]

dist=[[sys.maxsize]*k for _ in range(n+1)]
dist[1][0]=0

while q:
    cost, now=heapq.heappop(q)
    for nxt_node, nxt_cost in graph[now]:
        sCost=cost+nxt_cost
        if dist[nxt_node][k-1]>sCost:
            dist[nxt_node][k-1]=sCost
            dist[nxt_node].sort()
            heapq.heappush(q, [sCost, nxt_node])

for i in range(1, n+1):
    if dist[i][k-1]==sys.maxsize:
        print(-1)
    else:
        print(dist[i][k-1])

'''
최단거리 리스트를 k개의 row를 갖는 2차원 리스트로 정의한다.
새로운 경로 값과 비교해 새로운 경로 값이 더 작다면 최단거리 리스트 값을 업데이트한 후,
업데이트한 값과 해당 노드를 큐에 추가한다.
최종 출력값은 최단 거리 리스트의 k-1번째 값을 보고 출력하면 된다.
'''