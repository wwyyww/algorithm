#2251. 물통
#문제 링크 : https://www.acmicpc.net/problem/2251

#책 풀이

import sys
from collections import deque

sender=[0, 0, 1, 1, 2, 2]
receiver=[1, 2, 0, 2, 0, 1]

cup=list(map(int, sys.stdin.readline().split()))

visited=[[False for _ in range(201)] for _ in range(201)]
answer=[False]*201

queue=deque()
queue.append((0,0))
visited[0][0]=True
answer[cup[2]]=True

while queue:
    now=queue.popleft()
    a=now[0]
    b=now[1]
    c=cup[2]-a-b
    for i in range(6):
        next=[a,b,c]
        next[receiver[i]]+=next[sender[i]]
        next[sender[i]]=0
        if next[receiver[i]]>cup[receiver[i]]:
            next[sender[i]]=next[receiver[i]]-cup[receiver[i]]
            next[receiver[i]]=cup[receiver[i]]
        if not visited[next[0]][next[1]]:
            visited[next[0]][next[1]]=True
            queue.append((next[0], next[1]))
            if next[0]==0:
                answer[next[2]]=True


for i in range(201):
    if answer[i]:
        print(i, end=' ')


'''
sender와 receiver를 사용해 탐색을 편하게 할 수 있다.
방문 여부 리스트가 2차원인 이유는 큐에 노드를 넣을 때 (a, b) 형태를 사용하기 때문이다.
정수의 범위가 1부터 200이기 때문에 answer를 201만큼 만들어서 최종 결과값을 출력할 때 answer의 인덱스를 활용한다.
출발은 a, b가 0인 상태이기 때문에 (0, 0)으로 시작한다.
그 다음에는 모두 탐색하기 위해 6가지 케이스를 탐색한다.
물통의 값을 계산하고 넘치는 경우도 처리를 한다.
'''