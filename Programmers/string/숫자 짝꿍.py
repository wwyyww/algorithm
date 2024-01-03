#131128. 숫자 짝꿍
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131128?language=python3

#내 풀이

def solution(X, Y):
    answer = ''
    count_x = [0 for x in range(0, 10)]
    count_y = [0 for x in range(0, 10)]
        
    for x in X:
        count_x[int(x)] += 1
    
    for y in Y:
        count_y[int(y)] += 1
    
    for i in range(9, -1, -1):
        if count_x[i] * count_y[i] == 0:
            continue
        else:
            m = min(count_x[i], count_y[i])
            for _ in range(m):
                answer += str(i)
    
    if len(answer) == 0:
        return "-1"
    
    if answer[0] == "0":
        return "0"
    
    return answer

'''
처음에는 이중 반복문을 써서 X, Y 문자열을 모두 확인하는 방식으로 코드를 짰다.
근데 시간초과가 나서 리스트의 인덱스를 활용해 개수를 측정하는 방식으로 변경했다.
'''