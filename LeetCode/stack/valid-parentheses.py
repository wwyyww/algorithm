#20. Valid Parentheses
#문제 링크 : https://leetcode.com/problems/valid-parentheses/

#내 풀이
class Solution:
    def isValid(self, string: str) -> bool:
        stack=[]
        dic={')':'(', '}':'{',']':'['}
        
        for s in string:
            if not stack:
                stack.append(s)
                continue
                
            if s in dic and dic[s]==stack[-1]:
                stack.pop()
            else:
                stack.append(s)

            
        return not stack

'''
딕셔너리를 사용해서 괄호의 짝을 확인했다.
'''