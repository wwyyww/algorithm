#42576. 완주하지 못한 선수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42576

#내 풀이

from collections import Counter

def solution(participant, completion):

    p=Counter(participant)
    c=Counter(completion)
    p.subtract(c)

         
    return p.most_common(1)[0][0]