#12969. 직사각형 별찍기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12969

#내 풀이

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')