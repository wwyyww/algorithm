#12915. 문자열 내 마음대로 정렬하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12915

#다른 풀이 참고 : https://codingpractices.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%A7%88%EC%9D%8C%EB%8C%80%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(strings, n):
    strings.sort()
    tmp=[]
    for s in strings:
        tmp.append(s[n]+s)
    tmp.sort()
    answer=[]
    for t in tmp:
        answer.append(t[1:])
 
    return answer

'''
맨앞에 기준 문자를 넣고 이후에 원본 문자열을 넣어서 
기준문자열로 정렬하고 만약 기준 문자열이 같으면 사전순으로도 정렬이 된다.
'''