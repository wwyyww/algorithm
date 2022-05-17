#14. Longest Common Prefix
#문제 링크 : https://leetcode.com/problems/longest-common-prefix/

#내 풀이
import sys
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len=sys.maxsize
        for s in strs:
            min_len=min(len(s), min_len)
        output=''
        
        for i in range(min_len):
            check=strs[0][i]
            num=1
            for s in strs[1:]:
                if check==s[i]:
                    num+=1
            if num==len(strs):
                output+=check
            else:
                break
        
        
        return output 
                