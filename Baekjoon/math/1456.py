#1456. 거의 소수
#문제 링크 : https://www.acmicpc.net/problem/1456

#내 풀이 - 책 가이드라인 보고

import sys

a, b=map(int, sys.stdin.readline().split())

nums=[0 for i in range(10000001)]
output=0

for i in range(2, 10000001):
    if nums[i]==1:
        continue

    if nums[i]==0:
        for j in range(i+i, 10000001, i):
            nums[j]=1

for i in range(2, 10000001):
    if nums[i]==0:
        now=i
        while i<=b/now:
            if i>=a/now:
                output+=1
            now=now*i

print(output)

'''
책 가이드 보기 전에는 그냥 주어진 범위를 가지고 계산했는데 메모리 초과가 떴다.
책 가이드를 보니까 최대 범위인 10^14의 제곱근인 10^7 범위 안에 있는 소수는 다 구하고 시작했다.
그리고 거의 소수 구할 때 범위 안에 속하는지 확인하는 과정에서 표현 범위를 초과할 수도 있기 때문에
i*now<=b가 아니라 i<=b/now로 비교를 해야 한다.
'''