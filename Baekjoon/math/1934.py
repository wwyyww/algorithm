#1934. 최소공배수
#문제 링크 : https://www.acmicpc.net/problem/1934

#내 풀이

import sys

n=int(sys.stdin.readline())
gcd=1
remain=1

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ab=a*b
    while True:
        if b%a==0:
            gcd=a
            break
        else:
            remain=b%a
            b, a = a, remain

    print(int(ab/gcd))

'''
최소공배수는 a*b를 a, b의 최대공약수로 나눠서 구하면 된다. - 책 참고
처음에 코드를 짜서 제출했을 때 틀렸는데 내가 a,b를 변경했는데 결과값을 바뀐 a,b로 구하고 있어서
처음 a, b를 받았을 때 둘의 곱을 다른 변수에 저장하는 부분을 추가했다.
'''