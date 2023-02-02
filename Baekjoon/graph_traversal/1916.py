#1916. 최소비용 구하기
#문제 링크 : https://www.acmicpc.net/problem/1916

#내 풀이

import sys
import heapq

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end=map(int, sys.stdin.readline().split())
heap=[]
price=[sys.maxsize]*(n+1)
price[start]=0

visited=[False]*(n+1)

heapq.heappush(heap, (0, start))

while heap:
    now=heapq.heappop(heap)
    now_node=now[1]
    if visited[now_node]:
        continue
    visited[now_node]=True

    for node in graph[now_node]:
        nxt=node[0]
        nxt_price=node[1]
        if price[now_node]+nxt_price<price[nxt]:
            price[nxt]=price[now_node]+nxt_price
            heapq.heappush(heap, (price[nxt], nxt))

print(price[end])

'''
코드를 제출했는데 시간초과가 떠서 visited의 위치를 앞으로 바꿔서
방문한 노드라면 아래의 계산과정을 거치지 않게 했다.
'''