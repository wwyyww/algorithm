#1715. 카드 정렬하기
#문제 링크 : https://www.acmicpc.net/problem/1715

#내 풀이 - 책 참고

import sys
import heapq

n=int(sys.stdin.readline())
nums=[]
output=0

for _ in range(n):
    heapq.heappush(nums, int(sys.stdin.readline()))


while len(nums)>1:
    tmp=heapq.heappop(nums)+heapq.heappop(nums)
    output+=tmp
    heapq.heappush(nums, tmp)

    
print(output)

'''
우선순위 큐를 사용해서 코드를 짰는데 자꾸 출력초과가 떠서
책 가이드를 보고 while문으로 바꿨는데 틀렸다고 해서 책 코드를 보니까
누적하는 변수랑 두 수를 합치는 변수를 따로 두지 않아서 틀렸다.
'''

