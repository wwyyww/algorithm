#787. Cheapest Flights Within K Stops
#문제 링크 : https://leetcode.com/problems/cheapest-flights-within-k-stops/
#실패

#책 풀이
import collections
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1

'''
이전 문제와 같이 그래프를 구성하고 우선순위 큐를 사용해서 푼다.
앞의 문제(#743. Network Delay Time)와 다른 것을 정리해보자면

- 우선순위 큐에 남은 경유지 수가 추가됨
- node가 목적지에 도달했는지 확인하는 조건이 추가됨
- 아직 경유지를 더 거칠 수 있는지 확인하는 조건이 추가됨
- 방문했던 노드를 저장하는 변수 없음

'''