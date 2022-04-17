#406. Queue Reconstruction by Height
#문제 링크 : https://leetcode.com/problems/queue-reconstruction-by-height/

#책 풀이 : 우선순위 큐 사용
import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

'''
키 값을 음수로 넣어서 최대 힙 형태로 구현을 했다. 최대 힙이라서 heappop()을 하면 첫 번째 값이 큰 순서대로 추출이 된다.
두번째 값은 인덱스로 활용해서 해당 위치에 heappush로 삽입한다.
'''
