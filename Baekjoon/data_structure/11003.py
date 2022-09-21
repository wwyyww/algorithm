#11003. 최솟값 찾기
#문제 링크 : https://www.acmicpc.net/problem/11003

#내 풀이 - 시간 초과 실패
import sys
n, l = map(int, sys.stdin.readline().split())
nums = list(map(int, input().split()))

output=[]
start=0
end=1


for i in range(0, n):

    output.append(min(nums[start:end]))
    if end<l:
        end+=1
        continue
    start+=1
    end+=1
    

print(*output)

#책 풀이
from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))
for i in range(N):
    #deque의 가장 끝에 있는 값이 들어가야 될 값보다 큰 경우 pop으로 제거한다.
    while mydeque and mydeque[-1][0]>now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1]<=i-L: #범위가 아닌 값은 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')


'''
나는 min을 사용해서 풀었는데 시간초과로 실패했다.
책에서는 deque를 사용했다. deque는 속도가 빠르다.
deque에 값을 추가하기전에 크기 비교를 해서 크다면 값을 추가하지 않기 때문에
deque의 맨 앞에 있는 값이 최소값이다.
deque에 값을 넣을 때 (값, 인덱스) 형태로 넣어서 만약 범위에 해당하지 않는 값이라면
인덱스를 확인해서 제거한다.
'''