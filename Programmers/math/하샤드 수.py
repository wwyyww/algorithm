#12947. 하샤드 수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12947

#내 풀이

def solution(x):

    tmp=list(str(x))
    num=0
    for t in tmp:
        num+=int(t)
    if x%num==0:
        return True
    else:
        return False
