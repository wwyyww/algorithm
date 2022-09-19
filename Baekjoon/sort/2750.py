#2750. 수 정렬하기
#문제 링크 : https://www.acmicpc.net/problem/2750

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