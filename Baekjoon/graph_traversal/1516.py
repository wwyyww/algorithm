#1516. 게임 개발
#문제 링크 : https://www.acmicpc.net/problem/1516

#책 풀이

import sys
from collections import deque

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
time=[0]*(n+1)
degree=[0]*(n+1)
output=[0]*(n+1)

for i in range(1, n+1):
    nums=list(map(int, sys.stdin.readline().split()))
    time[i]=nums[0]
    del nums[0]
    for num in nums:
        if num==-1:
            break
        graph[num].append(i)
        degree[i]+=1

queue=deque()
for i in range(1, n+1):
    if degree[i]==0:
        queue.append(i)
    
while queue:
    start=queue.popleft()
    for node in graph[start]:
        output[node]=max(output[node], output[start]+time[start])
        # output[node]+=time[start]   => 내 풀이 - 실패
        degree[node]-=1
        if degree[node]==0:
            queue.append(node)

for i in range(1, n+1):
    print(output[i]+time[i])

'''
*위상 정렬 문제*
내가 시간 계산 부분에서 잘못했다.
시간 계산 부분에서 현재 노드에 저장된 시간과 이전 노드+현재 건물의 시간을 비교해서 최댓값을 넣어야 한다.
그 이유는 이미 세워져야 하는 건물이 결과값에 반영된 경우와 그렇지 않은 경우가 있기 때문이다.
'''