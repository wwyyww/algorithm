#1976. 여행 가자
#문제 링크 : https://www.acmicpc.net/problem/1976

#내 풀이

import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
city=list(range(201))
possible=True

def find(node):
    if city[node]==node:
        return node
    else:
        city[node]=find(city[node])
        return city[node]

def union(a, b):
    a=find(a)
    b=find(b)
    city[b]=city[a]

for i in range(1, n+1):
    nums=list(map(int, sys.stdin.readline().split()))
    for idx, num in enumerate(nums): # (1)
        if num==1:
            union(i, idx+1)

plans=deque(list(map(int, sys.stdin.readline().split())))
while len(plans)>1:
    first=plans.popleft()
    second=plans.popleft()
    a=find(first)
    b=find(second)
    if a!=b:
        possible=False
        break
    plans.appendleft(second)

if possible:
    print('YES')
else:
    print('NO')


'''
*유니온 파인드 문제*
문제에서 i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미한다고 했는데,
그 부분을 제대로 안 읽어서 (1) 부분을 인덱스를 안쓰고 num만 사용해서
union(i, num)으로 코드를 짰었다. 그래서 그 부분을 인덱스와 값을 모두 사용하게 수정했다.
'''