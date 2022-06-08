#17. Letter Combinations of a Phone Number
#문제 링크 : https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

#책 풀이
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        output=[]
        graph={'2':"abc", '3':"def", '4':"ghi", '5':"jkl",'6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        if not digits:
            return []
        
        def dfs(index, path):
            
            if len(path) == len(digits):
                output.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in graph[digits[i]]:
                    dfs(i+1, path+j)
        
        
        
        dfs(0, "")
                
            
        
        return output

'''
dfs 함수의 파라미터로 텍스트를 넘겨주면서 해당 텍스트에 추가하는 방식으로 진행한다.
조합한 문자열의 길이와 주어진 문자열의 길이가 같아지면 함수가 종료되면서 탐색을 종료한다.

'''