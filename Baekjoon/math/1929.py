#1929. 소수 구하기
#문제 링크 : https://www.acmicpc.net/problem/1929

#내 풀이 - 실패
import sys

m, n = map(int, sys.stdin.readline().split())
nums=[0 for i in range(n+1)]

for i in range(m, n+1):
    if i==1:
        nums[i]=1
        continue
        
    if nums[i]==0:
        for j in range(i+1, n+1):
            if j%i==0:
                nums[j]=1

for i in range(m, n+1):
    if nums[i]==0:
        print(i)



#책 풀이

import sys
import math

m, n = map(int, sys.stdin.readline().split())
nums=[0 for i in range(n+1)]
nums[1]=1

for i in range(2, int(math.sqrt(n))+1):
    if nums[i]==1:
        continue

    if nums[i]==0:
        for j in range(i+i, n+1, i):
            nums[j]=1

for i in range(m, n+1):
    if nums[i]==0:
        print(i)

'''
나는 그냥 정직하게 코드를 짰는데 시간초과가 떴다.
책 풀이를 보니까 우선 바깥에 있는 반복문의 종료범위를 제곱근으로 했기 때문에
횟수가 확 줄어들 수 있었다. 그리고 안쪽 반복문도 배수니까 1이 아닌 i를 더해나가는 방식을 사용했다.
'''