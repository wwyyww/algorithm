#11660. 구간 합 구하기 5
#문제 링크 : https://www.acmicpc.net/problem/11660

#내 풀이 - 실패
    
import sys
first=sys.stdin.readline
n,m=map(int, first().split())

sums=[[0 for i in range(n)]]
tmp=0
for i in range(0, n):
    empty=[]
    matrix=list(map(int, input().split()))
    for j in range(0, n):
        tmp=sums[i][j]+matrix[j]
        empty.append(tmp)
    sums.append(empty)
        

for i in range(m):
    second=sys.stdin.readline
    x1, x2, y1, y2=map(int, second().split())
    print(sums[n][x2-1]-sums[x2-1][x1-1]+sums[n][y1-1]-sums[x2-1][y1-1])


#책 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        #구간 합 구하기
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1 -1]
    print(result)

'''
책 풀이를 보니까 나는 아예 합배열을 잘못 생각해서 계산하고 있었다.
합 배열은 (0,0)을 기준으로 (x, y)까지의 영역에 있는 수의 합을 기준으로 만든다.
그렇게 합 배열을 만들면 훨씬 계산도 편해진다.
'''