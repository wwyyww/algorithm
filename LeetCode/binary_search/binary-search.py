#704. Binary Search
#문제 링크 : https://leetcode.com/problems/binary-search/submissions/

#내 풀이

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mid=len(nums)//2
        start=0
        end=len(nums)
        
        while start!=mid and end!=mid:
            if target>nums[mid]:
                start=mid
                mid=(end+mid)//2
            elif target<nums[mid]:
                end=mid
                mid=mid//2
            elif target==nums[mid]:
                return mid
        
        if target==nums[0]:
            return 0
        
        return -1

'''
하나만 있는 경우를 저렇게 처리해도 되는건지 모르겠지만 따로 조건을 확인하는 과정을 거치게했다.
반복문 조건을 처음에는 or로 했는데 그러면 start==mid가 되어도 end!=mid는 만족하지 않으니까
무한루프가 되었다. 그래서 and로 바꿔주었다.
'''

#책 풀이 - 1
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

'''
책에서는 left는 증가 right은 감소시키면서 mid의 범위를 조절한다.
left가 right보다 커지면 반복문을 빠져나간다.
'''

#책 풀이 - 2 : 이진 검색모듈
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

'''
이진검색 알고리즘을 지원하는 bisect 모듈을 사용하면 
이진검색 알고리즘을 구현하지 않고 간단하게 풀 수 있다.
'''