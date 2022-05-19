#150. Evaluate Reverse Polish Notation
#문제 링크 : https://leetcode.com/problems/evaluate-reverse-polish-notation/

#내 풀이
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        sign=['+', '-', '*', '/']
        stack=[]
        
        
        for t in tokens:
            if t not in sign:
                stack.append(t)
            if t in sign and len(stack)>1:
                stack.append(str(int(eval(stack.pop(-2)+t+stack.pop()))))
        
        return int(stack[-1])
