#8. String to Integer (atoi)
#문제 링크 : https://leetcode.com/problems/string-to-integer-atoi/

#내 풀이
class Solution:
    def myAtoi(self, s: str) -> int:

        sign=''
        output=''
        s=s.lstrip()
        
        for idx, letter in enumerate(s):
            if letter==' ' or letter.isalpha() or letter=='.':
                break
            if letter in ['-', '+'] and idx+1<len(s) and s[idx+1] in ['-', '+']:
                break
                
            elif letter in ['-', '+']:
                if len(output)>0:
                    break
                if letter=='-':
                    sign=letter
                continue
            
            if letter != '+':
                output+=letter
            
        if sign:
            output=sign+output
        
        if output=='' or output=='-':
            return 0
        
        output=int(output)
        if output>2**31-1:
            output=2**31-1
        elif output<-2**31:
            output=-2**31
        
        
        return output
                