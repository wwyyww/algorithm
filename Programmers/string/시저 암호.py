#12926. 시저 암호
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12926

#내 풀이

def solution(s, n):
    answer = ''
    # a=97 z=122 A=65 Z=90
    for i in s:
        tmp=ord(i)+n
        if i.lower() and tmp>122:
            tmp=(ord(i)+n)%96+70
        elif i.isupper() and tmp>90:
            tmp=(ord(i)+n)%64+38
        elif i==' ':
            tmp=32
        answer+=chr(tmp)
            
    
    return answer

'''
기본 테스트 케이스는 통과했는데 제출하니까 다 틀린걸로 나와서
찾아보니까 %26으로 계산하면 범위가 0~25로 나오는데 이때 내가 계산한 값을 더하면
범위가 틀릴 수 밖에 없었다. 만약에 %26으로 계산하려면 아스키값에서 A의 (소문자면 a) 아스키 값을
빼고 n을 더한 후에 26의 나머지를 구하고 거기에 다시 A의 아스키값을 더하면 된다.
'''