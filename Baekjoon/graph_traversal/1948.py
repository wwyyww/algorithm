#1948. 임계경로
#문제 링크 : https://www.acmicpc.net/problem/1948

#내 풀이 - 틀림
import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]
degree=[0]*(n+1)
output=[0]*(n+1)


for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b,c)) # (도착노드, 가중치)
    degree[b]+=1

start, end=map(int, sys.stdin.readline().split())
queue=deque()
queue.append(start)
road=[]

while queue:
    first=queue.popleft()
    #node : (도착노드, 가중치)
    for node in graph[first]:
        nxt=node[0]
        degree[nxt]-=1
        if output[nxt]>output[first]+node[1]:
            road.append(nxt)
        else:
            road.append(first)
        output[nxt]=max(output[nxt], output[first]+node[1])

        if degree[nxt]==0:
            queue.append(nxt)


print(output[end])
print(len(set(road)))


#책 풀이

import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]
reverse=[[] for _ in range(n+1)]
degree=[0]*(n+1)
output=[0]*(n+1)


for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph[a].append((b,c)) # (도착노드, 가중치)
    reverse[b].append((a,c))
    degree[b]+=1

start, end=map(int, sys.stdin.readline().split())
queue=deque()
queue.append(start)

while queue:
    first=queue.popleft()
    #node : (도착노드, 가중치)
    for node in graph[first]:
        nxt=node[0]
        degree[nxt]-=1
        output[nxt]=max(output[nxt], output[first]+node[1])

        if degree[nxt]==0:
            queue.append(nxt)

road=0
queue.clear()
queue.append(end)
visited=[False]*(n+1)
visited[end]=True

while queue:
    first=queue.popleft()
    for node in reverse[first]:
        if output[node[0]]+node[1]==output[first]:
            road+=1
            if not visited[node[0]]:
                visited[node[0]]=True
                queue.append(node[0])

print(output[end])
print(road)

'''
이들이 만나는 시간을 구하기 위해 max를 사용해 누적된 시간을 비교한다.
1분도 쉬지 않고 달려야 하는 도로의 수는 에지 뒤집기를 사용해서 구할 수 있다.
정방향 인접 리스트를 만들 때 역방향 인접 리스트도 생성한다.
위상 정렬을 하면서 임계 경로 값을 구한 후에 도착 도시에서 역방향으로 위상 정렬을 한다.
한 도시의 임계 경로값+시간이 이전 도시의 임계 경로값과 같은 경우에 해당 도로를 세어주고 도시를 큐에 삽입한다.
중복으로 도로를 세지 않기 위해 방문한 노드를 확인하면서 진행한다.
'''