#172928. 공원 산책
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172928

#내 풀이

def solution(park, routes):
    answer = []
    parks = [[-1 for x in range(len(park[0])+2)] for i in range(len(park)+2)]
    start = []
    
    for h, value in enumerate(park):
        for w, v in enumerate(value):
            if v == 'S':
                parks[h+1][w+1] = 0
                start = [h+1, w+1]
            elif v == 'O':
                parks[h+1][w+1] = 0
            elif v == 'X':
                parks[h+1][w+1] = -1
                    
    for route in routes:
        op, n = route.split(' ')
        n = int(n)
        if op == 'E':
            h, w = start[0], start[1]
            for i in range(n):
                w += 1
                if parks[h][w] == -1:
                    break
                elif i == n-1:
                    start[1] += n
        elif op == 'W':
            h, w = start[0], start[1]
            for i in range(n):
                w -= 1
                if parks[h][w] == -1:
                    break
                elif i == n-1:
                    start[1] -= n
            
        elif op == 'S':
            h, w = start[0], start[1]
            for i in range(n):
                h += 1
                if parks[h][w] == -1:
                    break
                elif i == n-1:
                    start[0] += n
        elif op == 'N':
            h, w = start[0], start[1]
            for i in range(n):
                h -= 1
                if parks[h][w] == -1:
                    break
                elif i == n-1:
                    start[0] -= n
    start[0] -= 1
    start[1] -= 1

    return start