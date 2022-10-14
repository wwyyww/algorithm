#1747. 소수&팰린드롬
#문제 링크 : https://www.acmicpc.net/problem/1747

#내 풀이

import sys

n=int(sys.stdin.readline())
nums=[0 for i in range(10000001)]
nums[1]=1

for i in range(2, 10000001):
    if nums[i]==1:
        continue
    else:
        for j in range(i+i, 10000001, i):
            nums[j]=1

for i in range(n, 10000001):
    if nums[i]==0:
        if str(i)==str(i)[::-1]:
            print(i)
            break

'''
최대 범위 설정은 책보고 했다.
최대 범위를 10^7로 한 이유는 N의 최댓값이 10^6이기 때문에
N이 10^6인 경우에 소수이면서 팰린드롬인 경우를 구하기 위해서다.
다른 풀이 찾아보니까 N의 범위가 1,000,000이라서 그 이상인 경우는
무조건 1003001을 출력하게 하는 방법도 있었다.
'''