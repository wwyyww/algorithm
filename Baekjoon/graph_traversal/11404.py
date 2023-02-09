#11404. 플로이드
#문제 링크 : https://www.acmicpc.net/problem/11404

#내 풀이 - 책 참고

import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

#최단거리 리스트
dist=[[sys.maxsize]*(n+1) for _ in range(n+1)] 

for i in range(1, n+1):
    dist[i][i]=0

for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    if dist[a][b]>c: #책 풀이 보고 추가한 부분
        dist[a][b]=c

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            dist[s][e]=min(dist[s][e], dist[s][k]+dist[k][e])

for s in range(1, n+1):
    for e in range(1, n+1):
        if dist[s][e]==sys.maxsize:
            dist[s][e]=0

for s in range(1, n+1):
    print(*dist[s][1:])



'''
*플로이드-워셜 알고리즘*

나는 버스 노선 데이터를 저장할 때 if문 없이 그냥 저장했기 때문에 틀렸다.
문제를 보면 노선은 1개가 아닐 수 있다는 말이 있기 때문에 같은 노선일 경우
더 적은 비용을 저장해야 하기 때문에 크기 비교가 필요하다.
'''