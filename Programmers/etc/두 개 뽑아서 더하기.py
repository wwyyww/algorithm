#68644. 두 개 뽑아서 더하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68644

#내 풀이

def solution(numbers):
    
    answer=[]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    answer=list(set(answer))
    return sorted(answer)