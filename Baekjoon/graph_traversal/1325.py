#1325. 효율적인 해킹
#문제 링크 : https://www.acmicpc.net/problem/1325

#내 풀이 - 책 참고

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
dist = [0]*(n+1)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
for v in range(1, n+1):
    search=deque()
    search.append(v)
    visited = [False]*(n+1)
    visited[v]=True
    while search:
        start=search.popleft()
        for node in graph[start]:
            if not visited[node]:
                visited[node]=True
                dist[node]+=1
                search.append(node)

mx=max(dist)
for i in range(1, n+1):
    if dist[i]==mx:
        print(i, end=' ')

'''
자꾸 틀렸길래 왜 틀렸나 했더니 내가 여기서 쓴 코드를 복붙안하고 틀렸던 코드에서 다른 부분을 자꾸 수정해서
이미 고쳤던 부분이 고치기 전 상태인 부분이 있어서 그랬다.
bfs 탐색을 진행해서 방문하는 노드에 값을 더해서 신뢰도를 측정한다.
그 다음에 신뢰도 값이 가장 큰 번호를 결과로 출력한다.
'''
