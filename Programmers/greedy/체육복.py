#42862. 체육복
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

#내 풀이

def solution(n, lost, reserve):
    newLost=[x for x in lost if x not in reserve]
    newReserve=[x for x in reserve if x not in lost]
    newLost.sort()
    answer=n-len(newLost)

    
    for l in newLost:
        if l-1 in newReserve:
            newReserve.remove(l-1)
            answer+=1
        elif l+1 in newReserve:
            newReserve.remove(l+1)
            answer+=1
    
    return answer