#11047. 동전 0
#문제 링크 : https://www.acmicpc.net/problem/11047

#내 풀이 - 책 가이드라인 보고
import sys

n, k = map(int, sys.stdin.readline().split())
nums=[]
output=0

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):
    if nums[i]<=k:
        output+=k//nums[i]
        k=k%nums[i]

print(output)

'''
큰 것부터 순서대로 계산했다.
'''