#12954. x만큼 간격이 있는 n개의 숫자
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12954

#내 풀이

def solution(x, n):
    answer = []
    tmp=x
    for i in range(n):
        answer.append(tmp)
        tmp+=x
    return answer