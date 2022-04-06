#179. Largest Number
#문제 링크 : https://leetcode.com/problems/largest-number/

#책 풀이 : 삽입 정렬
from typing import List


class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))

'''
to_swap은 두 숫자를 합쳤을 때 어떤 값이 더 큰지 비교하는 함수로
True면 스왑을 해야한다는 의미다.
삽입 정렬을 구현할 때는 인덱스는 1로 시작하고 인덱스-1로 이전 값과
비교를 하면서 정렬을 한다.
최종으로 반환할 때 join을 했다가 다시 int로 바꾸고 str로 변환하는 이유는
0인 경우때문이다. 0011로 반환될 수 있기 때문에 int로 0을 제거하고
다시 문자열로 변환해서 반환한다.
'''
