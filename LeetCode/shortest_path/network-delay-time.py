#743. Network Delay Time
#문제 링크 : https://leetcode.com/problems/network-delay-time/
#실패

#책 풀이 : 다익스트라 알고리즘
import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        #그래프 구성
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1

'''
이 문제에서 생각해야 하는 것

1. 모든 노드가 신호를 받는 데 걸리는 시간
2. 모든 노드를 도달할 수 있는가 ⇒ 모든 노드의 다익스트라 알고리즘 계산 값의 존재 여부로 판별가능

다익스트라 알고리즘을 구현할 때는 효율적인 방식을 위해 우선순위 큐를 적용해서 구현한다.

우선순위 큐를 사용하기 위해 저번에 그래프 문제를 풀 때 사용한 

#우선순위 큐란?

큐의 원소들이 우선순위를 가지고 있다. 
원래 큐는 먼저 들어온 원소가 먼저 나가는데 우선순위 큐에서는 우선순위가 높은 원소가 먼저 나간다.

- 그래프의 정점, 거리를 우선순위 큐에 삽입
- 우선순위 큐에서 최소 값 추출

times의 요소 출발노드, 도착노드, 소요시간을 그래프로 구성한다. 
그래프는 defaultdict를 사용해서 값이 리스트인 딕셔너리로 선언했다. 
Q는 우선순위 큐 변수로 소요시간, 정점으로 구성되어 있다. 주어진 출발 정점 k로 초기화를 한다.
우선순위 큐에서 pop을 하면 값이 가장 작은 것부터 pop된다. 

dist 변수는 방문한 노드를 저장하는 변수다. dist의 길이로 모든 노드에 도달했는지 확인한다. 
dist에 해당 노드의 키가 없을 때 우선순위 큐에서 pop된 노드의 값이 입력되는데, 우선순위 큐는 항상 값이 작은 것부터 pop이 된다.
따라서 dist에는 항상 해당 노드를 방문할 때 걸리는 시간 중 최소시간이 저장된다. 

만약 방문한 노드가 아니면 (시간, 노드)로 우선순위 큐에 값을 넣는다. 
우선순위 큐에서 값이 튜플일 때 튜플의 첫번째 항목을 기준으로 
우선순위가 계산되기 때문에 (시간, 노드) 순으로 넣어야 한다.

'''