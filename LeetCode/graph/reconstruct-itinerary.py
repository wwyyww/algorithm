#332. Reconstruct Itinerary
#문제 링크 : https://leetcode.com/problems/reconstruct-itinerary/

#책 풀이
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph=defaultdict(list)
        output=[]
        
        for ticket in sorted(tickets):
            graph[ticket[0]].append(ticket[1])
            

        def dfs(city):
            while graph[city]:
                dfs(graph[city].pop(0))
            output.append(city)
                
        
        
        dfs("JFK")

        
        return output[::-1]


'''
만약 경로가 여러개 나온다면 사전 순으로 출력해야 하기 때문에 정렬한 후에 그래프를 구성했다.
모든 티켓은 JFK로 시작해야 하기 때문에 dfs를 처음 호출할 때 지역을 JFK로 넣었다.
가장 마지막에 방문한 지역이 리스트 상에서는 제일 앞에 있기 때문에 최종 결과를 뒤집어서 리턴한다.
'''