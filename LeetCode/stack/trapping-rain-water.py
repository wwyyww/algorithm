#42. Trapping Rain Water
#문제 링크 : https://leetcode.com/problems/trapping-rain-water/

#책 풀이
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        stack=[]
        volume=0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top=stack.pop()

                if not len(stack):
                    break
                distance=i-stack[-1]-1  
                waters=min(height[i], height[stack[-1]])-height[top]

                volume+=distance*waters
            
            stack.append(i)
        
        return volume

'''
현재 높이가 이전 높이보다 높을 때를 기준으로 격차만큼 물 높이를 채운다.
거리를 확인하기 위해 인덱스 값을 스택에 넣는다.
'''