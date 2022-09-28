#13023. ABCDE
#문제 링크 : https://www.acmicpc.net/problem/13023

#내 풀이

import sys

n, m = map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n)]
visited=[False]*n
success=False

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num, depth):
    global success
    if depth==4:
        success=True
        print(1)
        return

    visited[num]=True
    for node in graph[num]:
        if not visited[node]:
            dfs(node, depth+1)
    visited[num]=False
    

for i in range(n):
    if success:
        break
    elif not visited[i]:
        dfs(i, 1)

if not success:
    print(0)

'''
자꾸 틀리길래 왜 그런가 봤더니 한 노드 탐색이 끝나고 나서
visited를 다시 False로 바꿔주지 않아서 그런거였다.
지금 탐색을 하나씩 차례대로 다 해주는데 false로 초기화를 안해주면 depth를 제대로 구할 수 없다.
'''