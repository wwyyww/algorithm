#1389. 케빈 베이컨의 6단계 법칙
#문제 링크 : https://www.acmicpc.net/problem/1389

#내 풀이 - 1 : heapq 사용

import sys
import heapq
from collections import deque

n, m = map(int, sys.stdin.readline().split())
nums = [[0]*(n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(p):
    q = deque([p])

    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[p][node]:
                q.append(node)
                nums[p][node] = nums[p][now] + 1
                visited[p][node] = True

for i in range(1, n+1):
    visited = [[False]*(n+1) for _ in range(n+1)]
    visited[i][i] = True
    bfs(i)


results = []
for i in range(1, n+1):
    results.append([sum(nums[i]), i])

heapq.heapify(results)
min_value = heapq.heappop(results)
print(min_value[1])


#내 풀이 - 2 : for문 사용

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
nums = [[0]*(n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(p):
    q = deque([p])

    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[p][node]:
                q.append(node)
                nums[p][node] = nums[p][now] + 1
                visited[p][node] = True

for i in range(1, n+1):
    visited = [[False]*(n+1) for _ in range(n+1)]
    visited[i][i] = True
    bfs(i)

results = []
for i in range(1, n+1):
    results.append(sum(nums[i]))

min_value = min(results)
for i in range(0, n):
    if results[i] == min_value:
        print(i+1)
        break

'''
처음에는 heapq를 써서 풀었는데 heapq가 없는 풀이랑 비교해보고 싶어서 둘 다 실행해봤다.
확인해보니까 heapq를 사용하지 않은 풀이가 시간도 적게 걸리고 메모리 사용량도 적었다.
'''