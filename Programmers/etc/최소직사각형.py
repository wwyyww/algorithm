#86491. 최소직사각형
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

#내 풀이

def solution(sizes):
    max_w = 0
    max_h = 0
    
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1])
    
    return max_w*max_h

'''
가로와 세로 값 중 더 큰 값은 항상 가로에 두고 최댓값을 계산한다.
'''