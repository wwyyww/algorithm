#241. Different Ways to Add Parentheses
#문제 링크 : https://leetcode.com/problems/different-ways-to-add-parentheses/

#책 풀이

from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                results.extend(compute(left, right, value))
        return results

'''
연산자를 기준으로 좌/우 분할을 한다.
분할된 값은 새로 정의한 compute 함수를 사용해 결과를 계산한다.
이때 extend 함수는 리스트에 값을 추가할 때 해당 값의 리스트를 풀어서 추가한다.
만약 [2, 3]을 빈 리스트에 append하면 [[2,3]]이 되는데 extend로 추가하면 [2, 3]이 된다.
분할 결과는 함수의 입력값이 숫자일 때 리턴하게 한다.
eval 함수는 문자열을 파싱해서 파이썬 표현식으로 처리해주기 때문에 계산이 된다.
'''