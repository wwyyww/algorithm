#12901. 2016년
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12901

#내 풀이

def solution(a, b):
    months=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days=["FRI","SAT", "SUN","MON","TUE","WED","THU"]
    tmp=0
    for i in range(1, a):
        tmp+=months[i]
    tmp+=b-1

    answer = days[tmp%7]
    return answer