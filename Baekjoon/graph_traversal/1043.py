#1043. 거짓말
#문제 링크 : https://www.acmicpc.net/problem/1043

#내 풀이 - 실패

'''
import sys
from collections import deque

n, m=map(int, sys.stdin.readline().split())
graph=list(range(51))

true=list(map(int, sys.stdin.readline().split()))
output=0

for t in range(true[0]):
    graph[true[t+1]]=-1

def find(node):
    if graph[node]==node:
        return node
    elif graph[node]==-1:
        return -1
    else:
        graph[node]=find(graph[node])
        return graph[node]

def union(a, b):
    a=find(a)
    b=find(b)
    graph[b]=graph[a]

for i in range(1, m+1):
    queue=deque(list(map(int, sys.stdin.readline().split())))
    start=queue.popleft()
    for _ in range(start):
        first=queue.popleft()
        if graph[first]==-1:
            while queue:
                second=queue.popleft()
                union(first, second)
            break
        else:
            queue.append(first)

for i in range(1, m+1):
    if graph[i]!=-1:
        output+=1

print(output)
'''


#책 풀이

import sys

n, m=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(m)]

true=list(map(int, sys.stdin.readline().split()))
t=true[0]
del true[0]
output=0

def find(node):
    if parent[node]==node:
        return node
    else:
        parent[node]=find(parent[node])
        return parent[node]

def union(a, b):
    a=find(a)
    b=find(b)
    parent[b]=a

parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i

for i in range(m):
    graph[i]=list(map(int, sys.stdin.readline().split()))
    del graph[i][0]


for i in range(m):
    firstPeople=graph[i][0]
    for j in range(1, len(graph[i])):
        union(firstPeople, graph[i][j])

for i in range(m):
    isPossible=True
    firstPeople=graph[i][0]
    for j in range(len(true)):
        if find(firstPeople)==find(true[j]):
            isPossible=False
            break
    if isPossible:
        output+=1


print(output)

'''
파티 정보를 저장해서 최종 결과값에 사용했어야 했는데 나는 파티 정보를 저장하지 않았다.
책에서는 주어지는 입력 리스트를 파티별로 저장하기 위해 2차원 리스트를 사용한다.
파티에 참가하는 사람 중 첫번째에 있는 사람을 대표 번호라고 생각해서 union 연산을 진행한다.
연산 진행 후에 파티 개수를 계산한다. 해당 파티의 대표 번호와 진실을 아는 사람들의 번호가 같은지
비교해서 가능한 파티를 계산한다.
'''