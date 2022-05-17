#13. Roman to Integer
#문제 링크 : https://leetcode.com/problems/roman-to-integer/

#내 풀이

class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dic2={'IV':4,'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        output=0
        idx=0
        while idx<len(s):

            if s[idx] in ['I', 'X', 'C'] and idx<len(s)-1:
                if s[idx:idx+2] in dic2:
                    output+=dic2[s[idx:idx+2]]
                    idx+=2
                    continue
            output+=dic[s[idx]]
            idx+=1
            

        
        return output

'''
딕셔너리를 활용해서 풀었다.
'''