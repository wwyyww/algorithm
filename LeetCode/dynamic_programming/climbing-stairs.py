#70. Climbing Stairs
#문제 링크 : https://leetcode.com/problems/climbing-stairs/

#책 풀이
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

