#1931. 회의실 배정
#문제 링크 : https://www.acmicpc.net/problem/1931

#내 풀이

import sys
import heapq

n=int(sys.stdin.readline())
meetings=[]
time=-1
output=0

for _ in range(n):
    a, b=map(int, sys.stdin.readline().split())
    heapq.heappush(meetings, (b, a))

for _ in range(n):
    now=heapq.heappop(meetings)
    if now[1]>=time:
        time=now[0]
        output+=1

print(output)

'''
종료시간이 적은 순으로 우선순위로 정렬되고 만약 종료 시간이 같다면 시작 시간이 빠른 순으로 정렬된다.
시작시간이 이전 종료시간 이후이면 결과값에 1을 더한다.
'''