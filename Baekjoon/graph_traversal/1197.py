#1197. 최소 스패닝 트리
#문제 링크 : https://www.acmicpc.net/problem/1197

#책 풀이

import sys
from queue import PriorityQueue

v, e=map(int, sys.stdin.readline().split())

q=PriorityQueue()
parent=[0]*(v+1)

for i in range(v+1):
    parent[i]=i

def find(node):
    if parent[node]==node:
        return node
    else:
        parent[node]=find(parent[node])
        return parent[node]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

for i in range(1, e+1):
    a, b, c=map(int, sys.stdin.readline().split())
    q.put((c, a, b))

output=0
edge=0

while edge<v-1:
    w, s, e=q.get()
    if find(s)!=find(e):
        union(s, e)
        edge+=1
        output+=w

print(output)

'''
대표 노드 리스트를 초기화하지 않아서 계속 시간초과가 났다.
우선순위 큐를 사용해서 따로 가중치를 정렬하는 코드를 짜지 않았다.
가장 앞에 있는 값을 우선순위로 사용하기 때문에 (가중치, 출발노드, 도착노드)순으로 값을 저장했다.
'''