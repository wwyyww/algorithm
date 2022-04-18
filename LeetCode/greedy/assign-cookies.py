#455. Assign Cookies
#문제 링크 : https://leetcode.com/problems/assign-cookies/

#내 풀이
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        gp=sp=0
        while gp<len(g) and sp<len(s):
            if g[gp]<=s[sp]:
                gp+=1
                sp+=1
            else:
                sp+=1
        return gp

'''
하나씩 비교해주었다. 책에서도 그리디 알고리즘을 사용해 같은 풀이를 했다.
'''
