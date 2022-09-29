#1920. 수 찾기
#문제 링크 : https://www.acmicpc.net/problem/1920

#내 풀이

import sys

n=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
nums.sort()

m=int(sys.stdin.readline())
find=list(map(int, sys.stdin.readline().split()))
is_find=[False]*m

for idx, f in enumerate(find):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if f<nums[mid]:
            end=mid-1
        elif f>nums[mid]:
            start=mid+1
        else:
            is_find[idx]=True
            break


for i in range(m):
    if is_find[i]:
        print(1)
    else:
        print(0)

'''
start, end 인덱스 사용하는 부분은 책을 참고했다.
책에서는 굳이 is_find 리스트를 만들지 않고 변수를 사용했다.
'''

