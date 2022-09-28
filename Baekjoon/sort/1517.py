#1517. 버블 소트
#문제 링크 : https://www.acmicpc.net/problem/1517

#내 풀이

import sys

n=int(sys.stdin.readline())
nums=list(map(int, input().split()))
tmp=[0]*n
result=0

def merge_sort(start, end):
    global result
    if end-start<1:
        return
    m=start+(end-start)//2
    
    merge_sort(start, m)
    merge_sort(m+1, end)

    for i in range(start, end+1):
        tmp[i]=nums[i]

    k=start
    one=start
    two=m+1

    while one<=m and two<=end:
        if tmp[one]>tmp[two]:
            nums[k]=tmp[two]
            result+=(two-k)
            k+=1
            two+=1
        else:
            nums[k]=tmp[one]
            k+=1
            one+=1
    
    while one<=m:
        nums[k]=tmp[one]
        k+=1
        one+=1
    while two<=end:
        nums[k]=tmp[two]
        k+=1
        two+=1

merge_sort(0, n-1)

print(result)

'''
지금 책이 병합정렬파트라서 이 문제를 병합 정렬로 구현한거지
만약에 그냥 이 문제를 풀었으면 그냥 버블 정렬로 풀어서
시간초과가 났을 것 같다.
'''