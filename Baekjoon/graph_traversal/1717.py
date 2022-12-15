#1717. 집합의 표현
#문제 링크 : https://www.acmicpc.net/problem/1717

#내 풀이

import sys
sys.setrecursionlimit(100000)
n, m=map(int, sys.stdin.readline().split())
graph=list(range(n+1))

def find(node):
    if node==graph[node]:
        return node
    else:
        graph[node]=find(graph[node]) # (1)
        return graph[node]


def union(a, b):
    rep_a=find(a)
    rep_b=find(b)
    graph[rep_b]=rep_a # (2)

for _ in range(m):
    f, a, b=map(int, sys.stdin.readline().split())
    if f==0:
        union(a, b)
    if f==1:
        rep_a=find(a)
        rep_b=find(b)
        if rep_a==rep_b:
            print('YES')
        else:
            print('NO')

'''
*유니온 파인드 문제*
자꾸 틀렸다고 나왔는데 그 이유가 (1), (2) 부분 때문이었다.
(1)에서 탐색한 대표 노드값을 바로 변경해야 하는데 다른 변수를 생성했어서 변경이 안되었다.
(2)에서는 선택된 노드가 아니라 선택된 노드의 대표 노드끼리 연결이 되어야 했는데 선택된 노드끼리 연결을 하고 있었다.

'''