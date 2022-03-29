#215. Kth Largest Element in an Array
#문제 링크 : https://leetcode.com/problems/kth-largest-element-in-an-array/

#내 풀이
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap=[]
        
        for num in nums:
            heapq.heappush(heap, num)
        
        for _ in range(0, len(nums)-k):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)

'''
heapq에 추가하고 작은 값부터 뺀 다음에 k번째로 큰 값이 가장 작은 값이 되게 만들었다.
'''

#책 풀이

'''
1. heapq 모듈의 heapify 사용
주어진 자료구조가 힙 특성을 만족하게 바꿔준다.

2. heapq 모듈의 nlargest 이용
k번째로 큰 값부터 순서대로 리스트로 반환해준다.

3. 정렬 사용
주어진 숫자를 정렬하고 인덱스로 접근하면 된다.
'''