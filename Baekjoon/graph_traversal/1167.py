#1167. 트리의 지름
#문제 링크 : https://www.acmicpc.net/problem/1167

#내 풀이 - 책 참고

import sys
from collections import deque

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
dists=[0]*(n+1)


for _ in range(n):
    nums=list(map(int, sys.stdin.readline().split()))
    idx=nums[0]
    for i in range(1, len(nums), 2):
        if nums[i]==-1:
            break
        graph[idx].append((nums[i], nums[i+1]))

def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        now=q.popleft()
        for node in graph[now]:
            idx=node[0]
            dist=node[1]
            if not visited[idx]:
                visited[idx]=True
                dists[idx]+=dists[now]+dist
                q.append(idx)
        
bfs(1)
mx=1
for i in range(2, n+1):
    if dists[i]>dists[mx]:
        mx=i
visited=[False]*(n+1)
dists=[0]*(n+1)
bfs(mx)

print(max(dists))

'''
BFS를 한번 더 하는 부분은 책을 참고했다.
BFS를 짜는 건 했는데 한번 BFS를 하고 나서 왜 BFS를 한번 더
하는지는 이해가 안간다. 그냥 한번해서는 그게 제일 긴 줄 몰라서 그런건가?
그런 것 같다...
'''