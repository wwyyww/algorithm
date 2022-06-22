#77. Combinations
#문제 링크 : https://leetcode.com/problems/combinations/

#내 풀이
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        output=[]
        
        def dfs(start, end, stack):

            if len(stack)==k:
                output.append(stack[:])
                return
            
            for i in range(start, n+1):
                stack.append(i)
                dfs(i+1, end+1, stack)
                stack.pop()
            
        
        dfs(1, 0, [])
        
        return output

'''
dfs 함수를 정의해서 재귀 호출을 통해 문제를 풀었다.
조합 리스트, 조합 시작 범위, 끝 범위를 함수 인자로 사용했다.
'''