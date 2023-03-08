#12935. 제일 작은 수 제거하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12935

#내 풀이

def solution(arr):
    if len(arr)==1:
        return [-1]
    
    idx=arr.index(min(arr))
    del arr[idx]
    
    return arr