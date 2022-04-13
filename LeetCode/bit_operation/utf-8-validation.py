#393. UTF-8 Validation
#문제 링크 : https://leetcode.com/problems/utf-8-validation/
'''
문제 : 
UTF-8 문자열인지 검증해야 한다.
1바이트 문자는 첫비트가 0이어야 한다.
n바이트 (n>=2) 이상의 문자열은 n개의 비트가 1, n+1번째 비트는 0이어야 한다.
n바이트를 제외한 나머지들은 10으로 시작해야 한다.
'''

#책 풀이 : 첫 바이트를 기준으로 판별
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True

'''
first는 첫바이트로 첫바이트의 앞부분에 1이 얼마나 있는지 편하게 확인하기 위해 시프트연산을 했다.
1~4바이트의 모든 경우를 각각 if문으로 나눠주었다.
check 함수는 해당 바이트만큼 10으로 시작하는지 확인하는 함수다.
나는 시도할 때 bin으로 변환해서 문자열 상태로 코드를 짰는데 책은 시프트연산을 통해 비트로 변환하고
각각 조건을 지정해서 계산했다.
'''
