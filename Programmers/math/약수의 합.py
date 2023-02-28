#12928. 약수의 합
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12928

#내 풀이

def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n%i==0:
            answer+=i
    
    
    return answer