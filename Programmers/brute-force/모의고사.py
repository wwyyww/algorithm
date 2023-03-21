#42840. 모의고사
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

#내 풀이

def solution(answers):
    answer = []
    a=[1, 2, 3, 4, 5]
    b=[2, 1, 2, 3, 2, 4, 2, 5]
    c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]

    for idx, i in enumerate(answers):
        if i==a[idx%5]:
            score[0]+=1
        if i==b[idx%8]:
            score[1]+=1
        if i==c[idx%10]:
            score[2]+=1
    
    mx=max(score)
    for i in range(3):
        if score[i]==mx:
            answer.append(i+1)
    

    return answer