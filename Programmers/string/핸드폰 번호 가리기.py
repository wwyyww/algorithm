#12948. 핸드폰 번호 가리기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12948

#내 풀이

def solution(phone_number):
    answer = ''
    for _ in range(len(phone_number)-4):
        answer+='*'
    answer+=phone_number[-4:]


    
    return answer