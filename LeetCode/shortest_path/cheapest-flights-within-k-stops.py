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

근데 이 코드 제출하면 시간초과 떠서 다른 풀이를 찾았다.
'''


#다른 풀이 - time limit exceed 안나는 풀이
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph=defaultdict(list)
        
        for s, d, p in flights:
            graph[s].append((d,p))
        
        q=[(0, src, K)]
        vis={}
        
        while q:
            price, node, k = heapq.heappop(q)
            
            if node==dst:
                return price
            
            if node not in vis or vis[node]<=k:
                vis[node]=k
                for d, p in graph[node]:
                    if k>=0:
                        tmp=price+p
                        heapq.heappush(q, (tmp, d, k-1))
        
        return -1

'''
방문한 노드를 확인하는 부분이 추가되었다. 다른 경로일 때 해당 노드를 재방문할 수 있어서
해당 노드를 방문하려면 더 적은 경유지를 거쳤어야 한다. 경유지의 수를 빼고 있기 때문에 >k가 아니라 <=k로 했다.
k가 0이상인 것을 확인해야 아직 최대 경유지 수를 초과하지 않았다는 것을 알 수 있다.

풀이참고 : https://8iggy.tistory.com/115
'''