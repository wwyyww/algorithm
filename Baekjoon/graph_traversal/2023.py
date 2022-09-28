#2023. 신기한 소수
#문제 링크 : https://www.acmicpc.net/problem/2023

#책 풀이 보고

import sys

n=int(sys.stdin.readline())
odds=[1,3,5,7,9]

def isPrime(num):
    for i in range(2, int(num/2)+1):
        if num%i==0:
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
        return
    else:
        for odd in odds:
            if isPrime(num*10+odd):
                dfs(num*10+odd)
        
dfs(2)
dfs(3)
dfs(5)
dfs(7)

'''
처음에 가이드만 보고 짜다가 시간 초과가 나길래 
책 풀이를 봤는데 소수 구하는 함수에서 끝 범위를 숫자 절반으로 해야했다.
나는 그냥 숫자로 끝범위 했는데 생각해보면 절반으로 나눠도 소수 여부는 확인가능하니까
굳이 숫자를 그대로 쓸 필요가 없었다.
'''