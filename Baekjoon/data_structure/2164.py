#2164. 카드2
#문제 링크 : https://www.acmicpc.net/problem/2164

#내 풀이

import sys
from collections import deque

n=int(sys.stdin.readline())
queue=deque(range(1, n+1))

while len(queue)>1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])


'''
deque 자체로 rotate 함수가 있길래 그걸 썼는데
정석은 popleft해서 append를 하는 게 맞는 것 같다.
'''