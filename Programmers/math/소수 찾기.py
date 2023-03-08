#12921. 소수 찾기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12921

#내 풀이

import math

def solution(n):
    answer = 0
    nums=[0]*(n+1)
    
    for i in range(2, n+1):
        nums[i]=i
    
    for i in range(2, int(math.sqrt(n))+1):
        if nums[i]==0:
            continue
        for j in range(i+i, n+1, i):
            nums[j]=0
    
    answer=n+1-nums.count(0)
    
    return answer

'''
소수찾기 = 에라토스테네스의 체
1. 구할 소수의 범위만큼 리스트 생성
2. 리스트 초기화
3. 현재 숫자의 배수에 해당하는 수를 탐색하면서 지운다.
=> 이때, 탐색 종료 범위는 끝 범위 숫자의 제곱근으로 설정한다.
'''