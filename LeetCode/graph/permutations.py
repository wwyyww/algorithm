#46. Permutations
#문제 링크 : https://leetcode.com/problems/permutations/submissions/

#책 풀이
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results=[]
        prev_elements=[]
        
        def dfs(elements):
            if len(elements)==0:
                results.append(prev_elements[:])
            
            for e in elements:
                next_elements=elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        
        return results

'''
이전 값인 prev_elements, 다음 값인 next_elements 변수가 있다. 
prev_elements에 현재값이 추가되고 남은 값들을 가지고 있는 next_elements를 넘기면서 dfs 함수를 재귀호출한다. 
자식노드가 0일때 결과값에 추가한다. 
pop은 순열 1개가 완성되고 나서 prev_elements를 빈 리스트로 만들기 위해서 있다.
결과를 추가할 때 prev_elements[:]로 하는 이유는 값을 추가하기 위해서다. 
만약 prev_elements로 하면 값이 할당되는 것이 아니라 참조가 할당된다.
'''