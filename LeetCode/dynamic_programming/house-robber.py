#198. House Robber
#문제 링크 : https://leetcode.com/problems/house-robber/

#책 풀이 : 타뷸레이션
import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]

'''
현재 짚과 옆집 숫자 중에 최댓값을 구하고 건넛집까지의 최댓값과 현재 집의 숫자값과의 합을 구해서
두 수 중 더 높은 값이 정답이 된다.
이 문제도 피보나치 수열과 비슷하게 풀면 된다.
우선 nums가 2이하일때 처리를 먼저 해준다.
결과는 딕셔너리에 넣는다. OrderedDict는 입력 순서가 유지되기 위해 사용한다. (파이썬 3.7이상은 자동으로 입력 순서가 유지된다.)
가장 끝 값을 추출하기 위해 popitem을 사용한다.

'''