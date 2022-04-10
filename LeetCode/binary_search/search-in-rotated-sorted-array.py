#33. Search in Rotated Sorted Array
#문제 링크 : https://leetcode.com/problems/search-in-rotated-sorted-array/

#책 풀이 : 피벗을 기준으로 이진검색

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        # 최소값 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1

'''
우선 피벗을 찾아야 한다. 피벗을 찾기 위해 최솟값을 찾는다.
최솟값은 이진 검색으로 구현한다. 
이제 피벗 위치를 알아냈으니 target을 찾기 위한 이진 검색을 한다.
mid_pivot은 비교 값의 기준이고 mid는 left와 right가 이동하는 기준이 된다.
잘 정렬되었을 때 기준으로 mid 인덱스에 있는 값이 지금은 mid_pivot 인덱스 위치에 있는 것이다.

'''