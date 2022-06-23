#39. Combination Sum
#문제 링크 : https://leetcode.com/problems/combination-sum/

#책 풀이
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output=[]
        prev_elements=[]
        
        def dfs(result, index, path):
            if result<0:
                return
            
            if result==0:
                output.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(result-candidates[i], i, path+[candidates[i]])
            
        
        
        dfs(target, 0, [])
        
        
        return output
            
'''
dfs 함수의 인자로 target에서 원소를 뺀 값, 인덱스, 탐색 경로를 사용한다.
조합이라서 원소 구성이 동일하면 순서와 상관없이 같은 것으로 본다.
그래서 중복 경우를 피하기 위해 인덱스를 사용해서 이미 나온 조합을 피한다.
'''