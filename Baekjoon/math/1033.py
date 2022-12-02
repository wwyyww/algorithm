#1033. 칵테일
#문제 링크 : https://www.acmicpc.net/problem/1033

#책 풀이

import sys

n=int(sys.stdin.readline())
nums=[[] for _ in range(n)]
visited=[False]*(n)
val=[0]*(n)
lcm=1

def gcd(a, b):
    if a<b:
        a, b = b, a

    if b==0:
        return a
    else:
        return gcd(b, a%b)

def dfs(node):
    visited[node]=True
    for num in nums[node]:
        nx=num[0]
        if not visited[nx]:
            val[nx]=val[node]*num[2]//num[1]
            dfs(nx)


for i in range(n-1):
    a, b, p, q=map(int, sys.stdin.readline().split())
    nums[a].append((b, p, q))
    nums[b].append((a, q, p))
    lcm*=(p*q//gcd(p,q))

val[0]=lcm
dfs(0)
allgcd=val[0]

for i in range(1, n):
    allgcd=gcd(allgcd, val[i])

for i in range(n):
    print(int(val[i]//allgcd), end=' ')

'''
그냥 내가 계산하면 어떻게 하는건지는 알겠는데 코드로 짤 때
어떤 방식을 사용해야 하는지 모르겠어서 책을 봤다.
그래프 관점으로 dfs를 하면 된다.
우선 서로의 비율을 알아야 하니까 그래프로 비율 정보를 저장한다.
그리고 나중에 비율을 계산하기 위해 최소 공배수 값을 계속 업데이트한다.
그 다음에는 dfs를 진행하면서 비율을 계산한다.
dfs가 다 진행된 후에는 모든 값의 최대공약수를 계산하고 최대공약수로 나눈 뒤 출력한다.

내가 책 코드를 보면서 작성했는데 자꾸 틀리길래 어디가 틀렸나 봤더니 35번 줄에서
그래프 값을 저장할 때 비율 순서를 바꿨어야 했는데 그냥 그대로 a, p, q로 저장해서 틀렸었다.

'''