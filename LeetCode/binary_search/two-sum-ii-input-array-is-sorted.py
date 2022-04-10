#167. Two Sum II - Input Array Is Sorted
#문제 링크 : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

#내 풀이
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right=0,len(numbers)-1
        output=[]
        
        while len(output)<2:
            if (numbers[left]+numbers[right])>target:
                right-=1
            elif (numbers[left]+numbers[right])<target:
                left+=1
            else:
                output.append(left+1)
                output.append(right+1)
        
        return output

'''
이전 문제 풀 때 방식 중 투포인터 방식을 사용해서 풀었다.
'''


#책 풀이 - 1 : 이진 검색

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1

'''
target에서 숫자값을 뺀 expected 값을 지정하고 해당 값을 이진 검색으로 찾는다.
'''

#책 풀이 - 2 : bisect 모듈 사용
import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1

'''
bisect_left는 정렬된 리스트(numbers)에 expected를 삽입할 위치를 리턴해준다. 
x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.
k+1은 탐색 범위를 지정해준것으로 k+1은 범위의 최솟값이다.
'''