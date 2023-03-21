#42748. K번째수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42748

#내 풀이

def solution(array, commands):
    answer=[]
    for command in commands:
        i, j, k=map(int, command)
        tmp=array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])

    return answer