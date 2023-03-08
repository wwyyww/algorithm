#12934. 정수 제곱근 판별
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12934

#내 풀이

import math
def solution(n):

    a=math.isqrt(n)
    if a*a==n:
        return (a+1)**2
    else:
        return -1