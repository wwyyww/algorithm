#78. Subsets
#문제 링크 : https://leetcode.com/problems/subsets/

#내 풀이
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        output=[]
        
        def dfs(index, path):
            output.append(path)
            
            if index==len(nums):
                return
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
                
            
        
        dfs(0, [])
        
        
        return output

'''
인덱스와 탐색 경로를 인자로 가지는 dfs 함수를 정의했다.
집합도 조합처럼 순서는 중요하지 않고 원소가 중요한 것이기 때문에 인덱스를 사용해서 접근했다.
'''