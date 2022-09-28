#2751. 수 정렬하기 2
#문제 링크 : https://www.acmicpc.net/problem/2751

#책 풀이
import sys

n=int(sys.stdin.readline())
nums=[]
tmp=[0]*(n)


for _ in range(n):
    nums.append(int(sys.stdin.readline()))


def merge_sort(start, end):
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

# merge_sort(1, n)
merge_sort(0, n-1)


for num in nums:
    print(num)

'''
분할은 재귀함수 형태로 진행해서 end-start가 1보다 작아지면 분할이 끝나고 정렬이 진행된다.
첫번째 while문은 두 그룹을 병합하는 부분이다. 
그 이후에 있는 두개의 while문은 남아있는 데이터를 정리하는 과정이다.
'''