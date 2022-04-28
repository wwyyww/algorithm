#53. Maximum Subarray
#문제 링크 : https://leetcode.com/problems/maximum-subarray/

#책 풀이 - 1 : 하향식 풀이(메모이제이션)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

'''
앞에서부터 값을 더하면서 누적 합을 계산하는데 0이하가 되면 버린다.
이렇게 값을 더한 결과값들에서 최댓값을 추출하면 된다.
'''

#책 풀이 - 2 : 카데인 알고리즘
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum

'''
이전 풀이에서는 매번 계산해서 넣고 마지막에 max를 사용했지만 
카데인 알고리즘은 매번 best_sum을 계산했다.
'''