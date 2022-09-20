#1546. 평균 
#문제 링크 : https://www.acmicpc.net/problem/1546

#내 풀이

import sys

n=int(sys.stdin.readline())
strs=sys.stdin.readline().strip().split(' ')
nums=[]
output=0
for num in strs:
    nums.append(int(num))
mx=max(nums)

output=sum(nums)/mx*100/n
print(output)

#책 풀이
n=input()
mylist=list(map(int, input().split()))
mymax=max(mylist)
sum=sum(mylist)
print(sum*100/mymax/int(n))

'''
책에서는 주어진 과목 점수를 map 함수를 사용해서 바로 int로 변환해 리스트로 만들었다.

**map(function, iterable)**
map 함수는 iterable의 모든 요소들에 function을 각각 적용해 반환한다.
반환 형태가 map이라서 list나 tuple 형식으로 변환이 필요하다.
'''