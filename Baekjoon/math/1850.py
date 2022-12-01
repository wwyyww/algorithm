#1850. 최대공약수
#문제 링크 : https://www.acmicpc.net/problem/1850

#내 풀이

import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)


result = gcd(b, a)
for _ in range(result):
    print(1, end='')


'''
처음에는 문제를 제대로 안읽고 그냥 최대공약수 구하는 문제라고 생각해서
그냥 최대공약수 구하는 코드를 짰는데 틀리길래 문제를 다시 읽어보니까
최대공약수만큼 1을 출력해야 했다.
그래서 출력부분을 추가했는데 처음에는 따로 문자열 변수를 만들어서 거기에 1을 더해주고
최종적으로 해당 값을 출력했는데, 시간 초과가 떴다.
그래서 그냥 end=''을 주고 print를 하니까 성공했다.
'''