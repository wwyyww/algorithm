#371. Sum of Two Integers
#문제 링크 : https://leetcode.com/problems/sum-of-two-integers/

#책 풀이 - 1 : 전가산기 구현
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # 전가산기 구현
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))
        if carry == 1:
            result.append('1')

        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        # 음수 처리
        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result

'''
마스크는 음수 처리를 위해 2의 보수로 만들어 주는 역할을 한다.
입력값을 정수로 가정했기 때문에 마스크 값은 0xFFFFFFFF이다.
마스크 값을 and 연산하면 2의 보수 값을 가지게 된다. 
zfill은 32비트 자릿수를 맞추기 위한 함수로 비어있는 곳을 모두 0으로 채워준다.

32비트로 가정했기 때문에 반복문도 32번 진행한다.
result이 낮은 자릿수부터 추가되었기 때문에 뒤집어 주는 작업을 하고 마스킹 작업을 진행한다.
음수인 경우에는 마스킹 값과 XOR을 하고 NOT으로 다시 음수를 만든다.

'''



#책 풀이 - 2 : 간단한 구현
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        # 합, 자릿수 처리
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 음수 처리
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a

'''
MASK는 2의 보수를 만들기 위한 것이다.
a에는 carry값이 반영되지 않는 a+b값이 저장되고 b에는 자릿수를 올려서 캐리 값이 담기게 했다.
음수에 대한 경우도 처리한다.
'''