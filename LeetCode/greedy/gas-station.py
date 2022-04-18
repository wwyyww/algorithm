#134. Gas Station
#문제 링크 : https://leetcode.com/problems/gas-station/

#내 풀이 : 실패한 풀이
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station=-1
        tank=0
        for i in range(0,len(gas)):
            idx=(i+1)%len(gas)
            if gas[i]>=cost[i] and gas[i]+gas[idx]>=cost[i]+cost[idx]:
                station=i
                tank=gas[i]-cost[i]
                break
        
        for i in range(station+1, station+len(gas)):
            idx=i%len(gas)
            tank+=gas[idx]-cost[idx]
            if tank<0:
                return -1
        
        return station
        
            
            


#책 풀이
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

'''
전체 기름의 양이 전체 비용보다 크다면 반드시 전체를 방문할 수 있는 출발점이 존재한다.
출발점이 안되는 곳이면 다음 인덱스로 이동한다. 그러면 자연스럽게 정답을 찾을 수 있다.
'''