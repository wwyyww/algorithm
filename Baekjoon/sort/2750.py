#2750. 수 정렬하기
#문제 링크 : https://www.acmicpc.net/problem/2750

#내 풀이 - 버블 정렬
import sys

n=int(sys.stdin.readline())
nums=[]
for _ in range(n):
    now=int(sys.stdin.readline())
    nums.append(now)

for i in range(0, n):
    for j in range(0, n-i):
        if j+1==n:
            break

        if nums[j]>nums[j+1]:
            nums[j+1], nums[j]=nums[j], nums[j+1]


for num in nums:
    print(num)

'''
처음에 j 시작 범위를 i로 해서 틀렸다.
탐색은 인덱스의 처음부터 시작하고 종료 범위가 점점 줄어들어야 한다. 
'''





#내 풀이
import sys
n=int(sys.stdin.readline())
nums=[]
for i in range(0, n):
    num=int(sys.stdin.readline())
    nums.append(num)

nums.sort()
for num in nums:
    print(num)

'''
파이썬의 sort 함수를 사용해서 정렬했다.
'''