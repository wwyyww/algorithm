#12940. 최대공약수와 최소공배수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12940

#내 풀이

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)



def solution(n, m):
    answer = []
    if n>m:
        n, m=m, n
    result=gcd(m, n)
    answer.append(result)
    answer.append(int(m*n/result))
    
    return answer

'''
최대공약수 = 유클리드 호제법
최소공배수=두수의 곱/최대공약수
'''