#2343. 기타 레슨
#문제 링크 : https://www.acmicpc.net/problem/2343

#책 풀이

import sys

n, m=map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))

start=max(nums)
end=sum(nums)

while start<=end:
    mid=int((start+end)/2)
    total=0
    count=0
    for i in range(n):
        if total+nums[i]>mid:
            count+=1
            total=0
        total+=nums[i]

    if total!=0:
        count+=1

    #블루레이 개수가 기준보다 더 많으면 start 값을 늘린다.
    if count>m:
        start=mid+1
    else:
        end=mid-1

print(start)            

'''
start 값은 강의 중 최대 길이, end값은 강의의 총 길이다.
만약 중간 값보다 총합이 크면 블루레이의 개수를 늘린다.
'''