#12932. 자연수 뒤집어 배열로 만들기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12932

#내 풀이

def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(int(i))

    answer.reverse()
    
    return answer