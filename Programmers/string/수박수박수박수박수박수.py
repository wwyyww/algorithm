#12922. 수박수박수박수박수박수?
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12922

#내 풀이

def solution(n):
    answer = ''
    even="수박"
    odd="수"
    if n%2==0:
        answer=even*(n//2)
    else:
        answer=even*(n//2)+odd
    
    return answer