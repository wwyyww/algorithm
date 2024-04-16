#16953. A → B
#문제 링크 : https://www.acmicpc.net/problem/16953

#내 풀이

import sys

a, b = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(100000)
count = []

def dfs(n, cnt):
    if n == b:
        count.append(cnt)
        return
    elif n < b:
        if 2*n <= b:
            dfs(2*n, cnt+1)
        if int(str(n)+'1') <= b:
            dfs(int(str(n) + '1'), cnt+1)

dfs(a, 0)

if count:
    print(min(count)+1)
else:
    print(-1)