#12917. 문자열 내림차순으로 배치하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12917

#내 풀이

def solution(s):
    answer = ''
    tmp=list(s)
    tmp.sort(reverse=True)
    answer=answer.join(tmp)
    
    return answer

'''
아스키 코드 값이 소문자가 더 크기 때문에 문자열을 리스트로 변경해서 sort를 사용했고
join으로 리스트를 문자열로 변경했다.
'''