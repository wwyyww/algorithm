#12931. 자릿수 더하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12931

#내 풀이

def solution(n):
    answer = 0

    for i in str(n):
        answer+=int(i)   
    

    return answer