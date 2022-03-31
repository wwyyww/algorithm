#56. Merge Intervals
#문제 링크 : https://leetcode.com/problems/merge-intervals/

#내 풀이 : 완성 X
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        output=[]
        intervals.sort(key=lambda x : x[0])
        
        for i in range(0, len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]: 
                if not output:
                    output.append([intervals[i][0], intervals[i+1][1]])
                    
                    continue
                
                for j in range(0, len(output)):
                    if output[j][1]>=intervals[i+1][1]:
                        output[j][1]=intervals[i+1][1]
                        
            elif i==(len(intervals)-2):
                output.append([intervals[i][0], intervals[i][1]])
                output.append([intervals[i+1][0], intervals[i+1][1]])
            else:
                output.append([intervals[i][0], intervals[i][1]])
                
        return output

'''
주어진 intervals를 정렬한 다음에 0,1->1,2 순으로 비교하는 방식이었는데
내가 잘못짠 부분이 0, 1이 병합되었으면 1,2에서 병합조건이 아니면 1자체가 output에 또 추가되는 부분이었다.

'''

#책 풀이 : 정렬 후 병합
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged

'''
정렬된 intervals의 아이템들이 merged의 마지막 원소의 종료범위보다 작다면
기존 merged 아이템과 병합을 하고 그렇지 않으면 해당 원소를 merged에 추가한다.
내가 잘못 생각한 부분은 병합된 리스트에서 마지막 원소를 확인하면 되는건데
병합된 리스트에 있는 원소들과 하나씩 비교하려고 했던 것이다.
'''
