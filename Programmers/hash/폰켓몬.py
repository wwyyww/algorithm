#1845. 폰켓몬
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845

#내 풀이

def solution(nums):
    answer = 0
    mx=int(len(nums)/2)
    unique=set(nums)
    if len(unique)>=mx:
        answer=mx
    else:
        answer=len(unique)
        
    
    return answer