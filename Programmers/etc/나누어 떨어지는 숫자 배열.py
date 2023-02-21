#12910. 나누어 떨어지는 숫자 배열
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12910

#내 풀이

def solution(arr, divisor):
    answer = []
    arr.sort()
    count=0
    
    for a in arr:
        if a%divisor==0:
            answer.append(a)
        else:
            count+=1
    if len(arr)==count:
        answer=[-1]
    
    return answer