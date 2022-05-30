#207. Course Schedule
#문제 링크 : https://leetcode.com/problems/course-schedule/

#책 풀이

import collections
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=collections.defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced=set()
        visited=set()
        
        def dfs(i):
            
            #순환구조인 경우
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True

'''
딕셔너리를 사용해서 그래프를 구성한다.
순환구조를 확인하기 위한 traced, 방문한 노드 확인하기 위한 visited
만약 순환구조면 False 반환, 방문한 노드면 True 반환

'''