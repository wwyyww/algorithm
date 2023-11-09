#42626. 더 맵게
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42626

#내 풀이

import heapq


def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville)>1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer+=1
        
    if scoville[0] < K:
        return -1
    
    
    return answer

'''
풀이 과정

1. 스코빌 지수가 가장 낮은 2개의 음식을 섞어 새로운 음식 만들기
2. 음식을 힙에 넣어서 맨 앞에 작은 값이 오게 하기 
3. 반복문을 빠져 나왔는데 가장 작은 스코빌 지수가 K보다 작다면 -1 반환하기

'''