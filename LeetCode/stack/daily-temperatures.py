#739. Daily Temperatures
#문제 링크 : https://leetcode.com/problems/daily-temperatures/

#내 풀이
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output=[0 for i in range(len(temperatures))]
        stack=[]
        
        for i, t in enumerate(temperatures):
            
            while stack and t>temperatures[stack[-1]]:
                out=stack.pop()
                output[out]=i-out
            stack.append(i)
                
                
            
        return output

'''
책을 참고해서 풀었다.
trapping-rain-water 문제처럼 인덱스를 스택에 추가해서 문제를 풀었다.
'''