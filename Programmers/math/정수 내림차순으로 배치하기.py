#12933. 정수 내림차순으로 배치하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12933

#내 풀이

def solution(n):
    answer = ''
    tmp=[]
    for i in list(str(n)):
        tmp.append(int(i))
    tmp.sort(reverse=True)
    for t in tmp:
        answer+=str(t)
    
    answer=int(answer)
        
    return answer