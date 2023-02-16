#12903. 가운데 글자 가져오기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12903

#내 풀이

def solution(s):
    if len(s)%2==1:
        answer=s[int(len(s)/2)]
    else:
        answer=s[int(len(s)/2)-1:int(len(s)/2)+1]
    return answer