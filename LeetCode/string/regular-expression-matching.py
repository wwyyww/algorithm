#10. Regular Expression Matching
#문제 링크 : https://leetcode.com/problems/regular-expression-matching/

#내 풀이
import re
class Solution:
    def isMatch(self, string: str, p: str) -> bool:
        
        result = re.match(p, string)
        if result and result.group(0)==string:
            return True
'''
파이썬이 제공해주는 re 모듈을 사용해서 풀었다.
'''

#다른 사람 풀이
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[0]*(lenP) for i in range(lenS)]
        dp[0][0] = 1

        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

        return bool(dp[-1][-1])

'''
다이나믹 프로그래밍으로 푼 풀이다.
'''
