#509. Fibonacci Number
#문제 링크 : https://leetcode.com/problems/fibonacci-number/submissions/

#내 풀이


class Solution:
    def fib(self, n: int) -> int:
        a=[0, 1]
        if n<2:
            return n
        
        for i in range(2, n+1):
            a.append(a[i-1]+a[i-2])
        
        return a[-1]

'''
0과 1을 리스트에 넣어두고 2부터 반복문으로 더했다.
책 풀이와 구조가 비슷하다. 책은 리스트가 아니라 defaultdict로 미리 공간을 잡아두었다.
'''

#책 풀이 - 1 : 메모이제이션 (하향식풀이)
import collections


class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]

'''
defaultdict로 계산한 값을 저장할 공간을 만들었다.
재귀로 계산하는데 이미 계산한 값은 딕셔너리에 저장된 값으로 바로 리턴한다.
한번 계산한 결과는 다시 안해도 되기 대문에 효율적이다.
'''

#책 풀이 - 2 : 딕셔너리 없이 변수만 사용
class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x