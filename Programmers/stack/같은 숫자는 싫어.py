#12906. 같은 숫자는 싫어
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12906

#내 풀이

def solution(arr):
    answer = []
    
    for a in arr:
        if not answer:
            answer.append(a)
            continue
        if answer[-1]==a:
            continue
        else:
            answer.append(a)
    
    return answer