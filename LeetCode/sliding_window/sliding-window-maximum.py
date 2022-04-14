#239. Sliding Window Maximum
#문제 링크 : https://leetcode.com/problems/sliding-window-maximum/

#내 풀이
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        start, end = 0, k-1
        
        while end<len(nums)-1:
            output.append(max(nums[start:end+1]))
            start+=1
            end+=1
        output.append(max(nums[start:]))
        return output

'''
이렇게 했는데 time limit exceeded가 뜬다.
'''

#책 풀이 : 큐를 이용한 최적화
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최대값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        return results

'''
최댓값 계산 부분을 최적화할 수 있다. 이전의 최댓값을 저장했다가 슬라이딩 윈도우를 이동했을때
들어온 새로운 값과 최댓값을 비교하고 최댓값이 윈도우 범위를 벗어났을 때 다시 계산하는 방식으로
계산량을 줄일 수 있다. 
최댓값에는 시스템이 지정할 수 있는 가장 낮은 값을 지저해서 초기화를 한다.
'''
