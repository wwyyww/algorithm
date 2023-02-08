#11657. 타임머신
#문제 링크 : https://www.acmicpc.net/problem/11657

#책 풀이

import sys

n,m=map(int, sys.stdin.readline().split())
edges=[]

dist=[sys.maxsize]*(n+1) #최단거리 리스트 초기화
dist[1]=0

for i in range(m):
    start, end, time=map(int, sys.stdin.readline().split())
    edges.append((start, end, time))



for _ in range(n-1):
    for start, end, time in edges:
        if dist[start]!=sys.maxsize and dist[end]>dist[start]+time:
            dist[end]=dist[start]+time
        
        
#음수 사이클 확인
mCycle=False

for start, end, time in edges:
    if dist[start]!=sys.maxsize and dist[end]>dist[start]+time:
        mCycle=True

if not mCycle:
    for i in range(2, n+1):
        if dist[i]!=sys.maxsize:
            print(dist[i])
        else:
            print(-1)
else:
    print(-1)        



'''
*벨만포드 알고리즘*
문제에 '시간 C가 양수가 아닐 때가 있다'라는 말이 있기 때문에 벨만-포드 알고리즘을 사용하면 된다.
1. 그래프 구현
2. 최단 거리 업데이트
3. 음수 사이클 확인

내가 생각한 구현방식과 다른 점
- 그래프 구현 방식이 다름 : 나는 원래 하던대로 2차원 리스트를 사용하려고 했는데 1차원 리스트를 사용해서 그래프를 구현함
'''