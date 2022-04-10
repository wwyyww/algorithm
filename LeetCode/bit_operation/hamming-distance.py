#461. Hamming Distance
#문제 링크 : https://leetcode.com/problems/hamming-distance/

#내 풀이
from collections import Counter
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        result=bin(x^y)
        c=Counter(result)
        return c['1']
        
'''
XOR을 해서 1이면 두 비트가 다르다는 의미이기 때문에
문자열 1의 개수를 반환했다.
'''

#책 풀이
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
'''
책은 count 함수를 사용했다.
'''