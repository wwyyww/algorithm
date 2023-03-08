#12930. 이상한 문자 만들기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12930

#내 풀이

def solution(s):
    answer = ''
    words=s.split(' ')
    
    for word in words:
        tmp=list(word)
        for idx, w in enumerate(tmp):
            if idx%2==0:
                tmp[idx]=w.upper()
            else:
                tmp[idx]=w.lower()
            
        answer+=''.join(tmp)+' '
    
    
    return answer[:-1]

'''
원래 rstrip으로 마지막 공백을 제거했는데, 문자열 자체에 맨 끝에 공백이 있는 경우가
있을 수 있어서 인덱스로 처리했다.
'''