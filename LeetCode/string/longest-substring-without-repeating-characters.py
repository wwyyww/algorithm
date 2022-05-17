#3. Longest Substring Without Repeating Characters
#문제 링크 : https://leetcode.com/problems/longest-substring-without-repeating-characters/

#내 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        
        if len(s)<2:
            return len(s)
        
        max_size=1
        
        while right<len(s):
                
            if s[right] not in s[left:right]:
                max_size=max(right-left+1, max_size)
                right+=1
            else:
                left+=1
                
        
        return max_size
            
'''

'''