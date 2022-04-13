#191. Number of 1 Bits
#문제 링크 : https://leetcode.com/problems/number-of-1-bits/

#책 풀이 - 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

'''
bin으로 숫자를 감싸면 문자열이 되기 때문에 count 함수를 사용하면 된다.
'''

#책 풀이 - 2 : 비트 연산
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count

'''
이진수의 특징으로 한 이진수에서 1을 뺀 값과 그 이진수를 and 연산하면
비트가 1씩 빠지게 되는 특징이 있다.
그 특징을 활용해서 n이 0이 될때까지 and연산을 해서 반복횟수를 계산한다.
'''
