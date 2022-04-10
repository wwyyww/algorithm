#136. Single Number
#문제 링크 : https://leetcode.com/problems/single-number/

#내 풀이
from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        c=Counter(nums)
        
        return c.most_common()[-1][0]
        
'''
비트 조작 첫문제라 감이 안와서 그냥 Counter 객체 써서 풀었다.
'''

#책 풀이 : XOR
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result

'''
단 1개의 원소를 찾기 적당한 연산자가 XOR이다.
XOR은 입력값이 같으면 False, 다르면 True이기 때문에
두번 나온 원소들은 0으로 초기화되고 한번 나온 원소만 남게 된다.
'''