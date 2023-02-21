#12912. 두 정수 사이의 합
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12912

#내 풀이

def solution(a, b):
    answer = 0
    if a>b:
        a, b=b, a
    elif a==b:
        return a
    answer=sum(list(range(a, b+1)))
    
    
    return answer