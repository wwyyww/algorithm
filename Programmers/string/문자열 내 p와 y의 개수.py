#12916. 문자열 내 p와 y의 개수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12916

#내 풀이

def solution(s):
    s=s.lower()
    p,y=0,0
    
    for i in s:
        if i=='p':
            p+=1
            continue
        elif i=='y':
            y+=1
            
    if p==y:
        return True
    else:
        return False