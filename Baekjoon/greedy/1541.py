#1541. 잃어버린 괄호
#문제 링크 : https://www.acmicpc.net/problem/1541

#책 풀이

import sys

nums=sys.stdin.readline().split('-')
output=0

def plus(num):
    plus=list(map(int, num.split('+')))
    total=0
    for p in plus:
        total+=p
    return total



for i in range(len(nums)):
    result=plus(nums[i])
    if i==0:
        output+=result
    else:
        output-=result

print(output)

'''
나는 처음에 숫자를 분리하고 부호를 또 따로 분리해서 계산을 해야한다고 생각해서 아예 방향을 잘못 잡았다.
책 풀이의 핵심 아이디어는 가능한 큰 수를 빼는 것이다. 따라서 최대한 다 더한 후 더한 값을 빼는 방식이다.
그래서 -를 기준으로 분리하고 그 이후에 함수를 사용해 + 기준으로 분리하고 그 수들을 다 더한다.
'''