#2252. 줄 세우기
#문제 링크 : https://www.acmicpc.net/problem/2252

#내 풀이

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

degree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
output=[]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    degree[b]+=1

queue=deque()

for i in range(1, n+1):
    if degree[i]==0:
        queue.append(i)

while queue:
    start=queue.popleft()
    output.append(start)
    for node in graph[start]:
        degree[node]-=1
        if degree[node]==0:
            queue.append(node)

print(*output)

'''
*위상 정렬 문제*

주어진 값을 2차원 리스트에 저장해서 그래프를 표현했다.
degree는 진입 차수를 계산하기 위한 변수다.
진입 차수가 0인 노드들을 먼저 큐에 저장하고 해당 노드의 인접 노드에 접근하면
진입 차수에서 1을 빼고 만약 진입 차수가 0이 되면 큐에 저장하는 방식이다.
'''