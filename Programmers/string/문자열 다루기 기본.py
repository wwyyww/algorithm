#12918. 문자열 다루기 기본
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12918

#내 풀이

def solution(s):
    if len(s)==4 or len(s)==6:
        return s.isdecimal()
    else:
        return False
