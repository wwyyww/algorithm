#10989. 수 정렬하기 3
#문제 링크 : https://www.acmicpc.net/problem/10989

#내 풀이 - 책 가이드라인 보고
import sys

n=int(sys.stdin.readline())
nums=[0]*10001

for _ in range(n):
    nums[int(sys.stdin.readline())]+=1


for i in range(10001):
    if nums[i]!=0:
        for _ in range(nums[i]):
            print(i)
    
'''
계수정렬 방식 사용.
수의 범위만큼 리스트를 만들고 그 인덱스를 숫자라고 생각해서
해당하는 숫자의 개수를 늘리고 출력할 때는 인덱스를 출력하는 방식이다.
'''