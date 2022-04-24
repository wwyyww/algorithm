#169. Majority Element
#문제 링크 : https://leetcode.com/problems/majority-element/

#내 풀이
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        return c.most_common(1)[0][0]

'''
Counter 객체를 사용해서 풀었다.
'''

#책 풀이 : 분할 정복
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

'''
우선 a와 b로 분할을 한다. 재귀를 통한 분할이기 때문에 리턴해주는 부분이 필요하다.
마지막 리턴 부분은 정복에 해당하는 부분이다.
만약 a가 과반수라면 인덱스가 1이기 때문에 a를 리턴한다. 이외에는 b를 리턴한다.
'''

