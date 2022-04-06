#973. K Closest Points to Origin
#문제 링크 : https://leetcode.com/problems/k-closest-points-to-origin/

#내 풀이
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist=[]
        output=[]
        for idx, point in enumerate(points):
            x, y = point[0], point[1]
            dist.append((x**2+y**2, idx))
        dist.sort(key=lambda x: x[0])

        
        for i in range(0, k):
            output.append(points[dist[i][1]])
        
            
        
        return output
            
'''
sort 함수를 사용해서 정렬했다.
'''

#책 풀이 : 우선순위 큐
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result

'''
k번 추출이라는 말을 보고 우선순위 큐를 떠올려야 한다.
우선순위 큐니까 heapq 모듈으로 구현한다.
우선순위 큐에 유클리드 거리 값을 넣고 좌표도 함께 넣어준다.
'''