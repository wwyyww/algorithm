#70. Climbing Stairs
#문제 링크 : https://leetcode.com/problems/climbing-stairs/

#책 풀이 : 메모이제이션(하향식 풀이)
import collections


class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


'''
피보나치 수와 동일한 유형의 문제다.
가장 작은 수부터 계산해서 해결한다.
만약 2이하면 방법의 수가 그 수와 동일하기 때문에 그 수를 반환한다.
'''