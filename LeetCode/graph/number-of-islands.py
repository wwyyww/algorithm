#200. Number of Islands
#문제 링크 : https://leetcode.com/problems/number-of-islands/

#책 풀이
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island=0
        
        def dfs(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
                return
            grid[i][j]=0
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i, j)
                    island+=1
        
        return island


'''
dfs 함수를 만들어서 해당 섬의 동서남북을 확인하기 위해 함수 내에서 dfs 함수를 또 호출한다.
한번 방문을 하면 값을 0으로 만들어서 중복되는 일이 없게 한다.
탐색이 끝나면 섬을 하나 발견한 것이기 때문에 섬 개수에 1을 더한다.
'''