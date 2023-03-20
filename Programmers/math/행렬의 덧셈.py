#12950. 행렬의 덧셈
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12950

#내 풀이

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp=[]
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)    

    
    return answer