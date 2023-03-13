#12943. 콜라츠 추측
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12943

#내 풀이

def solution(num):
    answer = 0
    cnt=0
    if num==1:
        return 0
    
    while num!=1 and cnt<=500:
        if num%2==0:
            num=int(num/2)
        else:
            num=num*3+1
        cnt+=1
    
    if cnt>500:
        return -1
    
    return cnt