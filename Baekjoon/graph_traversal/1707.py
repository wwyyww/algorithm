#1707. 이분 그래프
#문제 링크 : https://www.acmicpc.net/problem/1707

#책 풀이

import sys

n=int(sys.stdin.readline())
isEven=True
sys.setrecursionlimit(10**6)


def dfs(node):
    global isEven
    visited[node]=True
    for n in graph[node]:
        if not visited[n]:
            check[n]=(check[node]+1)%2
            dfs(n)
        elif check[n]==check[node]:
            isEven=False



for _ in range(n):
    v, e = map(int, sys.stdin.readline().split())
    visited=[False]*(v+1)
    check=[0]*(v+1)
    isEven=True
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v+1):
        if isEven:
            dfs(i)
        else:
            break
    if isEven:
        print('YES')
    else:
        print('NO')

    
        



'''
이미 방문한 노드에 다시 방문했을 때 해당 노드의 집합이 현재 노드의 집합과 같다면 이분 그래프가 불가능하다.
탐색을 할 때는 dfs 탐색으로 진행한다. 각 노드를 탐색할 때 두 집합으로 분할을 하면서 진행한다.
두 집합으로 분할을 진행할 때는 나머지 연산을 활용해 0과 1로 구분한다.
그래프는 방향이 없기 때문에 두 노드 모두에 값을 추가해서 그래프를 구성한다.
'''