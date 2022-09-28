#11724. 연결 요소의 개수
#문제 링크 : https://www.acmicpc.net/problem/11724

#내 풀이 - 책 가이드 보고
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
result=1

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(idx):
    visited[idx]=True
    for node in graph[idx]:
        if not visited[node]:
            dfs(node)

dfs(1)

for i in range(1, n+1):
    if not visited[i]:
        result+=1
        dfs(i)

print(result)

'''
처음에 제출했는데 recursion error가 나서 검색해보니까 
setrecursionlimit을 늘려주면 된다고해서 늘리니까 해당 오류가 해결되었다.
오류는 해결했었는데 틀렸다고 떠서 보니까 해당 그래프는 방향이 없어서 그래프에 값을 넣을 때
한쪽만 넣는게 아니라 양방향 다 넣어야했다.
'''