#84. Largest Rectangle in Histogram
#문제 링크 : https://leetcode.com/problems/largest-rectangle-in-histogram/

#다른 사람 풀이 : https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/476068/6-line-clean-O(N)-solution-stack-Python


from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[-1]
        heights.append(-1)
        mx=0
        
        for i, h in enumerate(heights):
            while stack and stack[-1] >=0 and h<=heights[stack[-1]]:
                mx=max(heights[stack.pop()]*(i-stack[-1]-1), mx)
            
            stack.append(i)
        
        return mx