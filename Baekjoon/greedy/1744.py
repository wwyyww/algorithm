#1744. 수 묶기
#문제 링크 : https://www.acmicpc.net/problem/1744

#내 풀이 - 실패

import sys
import heapq

n=int(sys.stdin.readline())
nums=[]
output=0

for _ in range(n):
    heapq.heappush(nums, -int(sys.stdin.readline()))

while len(nums)>0:
    if len(nums)>1:
        num1=heapq.heappop(nums)*(-1)
        num2=heapq.heappop(nums)*(-1)
        tmp=num1*num2
        if num1*num2>=num1+num2:
            output+=tmp
        elif num1>=num2:
            output+=num1
            heapq.heappush(nums, -num2)
        elif num1<num2:
            output+=num2
            heapq.heappush(nums, -num1)
        else:
            heapq.heappush(nums, -num2)
            heapq.heappush(nums, -num1)
    else:
        output+=heapq.heappop(nums)*(-1)



print(output)
        

#책 풀이
import sys
import heapq

n=int(sys.stdin.readline())
plus=[]
minus=[]
zero=0
one=0
output=0

for _ in range(n):
    num=int(sys.stdin.readline())
    if num>1:
        heapq.heappush(plus, -num)
    elif num==0:
        zero+=1
    elif num==1:
        one+=1
    else:
        heapq.heappush(minus, num)


while len(plus)>1:
    num1=heapq.heappop(plus)*(-1)
    num2=heapq.heappop(plus)*(-1)
    output+=num1*num2

if len(plus)>0:
    output+=heapq.heappop(plus)*(-1)

while len(minus)>1:
    num1=heapq.heappop(minus)
    num2=heapq.heappop(minus)
    output+=num1*num2

if len(minus) and zero==0:
    output+=heapq.heappop(minus)

output+=one


print(output)

'''
나는 그냥 if문으로 나누어서 코드를 짰는데 틀렸다.
음수, 양수, 1, 0을 분리해서 계산하니까 훨씬 코드도 간단하다.
양수는 우선순위 큐에 넣을 때 음수로 만들어서 넣는다. 절댓값이 큰 값부터 pop하기 위해서.
'''