#11720. 숫자의 합
#문제 링크 : https://www.acmicpc.net/problem/11720

#내 풀이

import sys

n=int(sys.stdin.readline())
num=list(sys.stdin.readline())
result=0

for i in range(0, n):
    result+=int(num[i])

print(result)

'''
처음에는 숫자가 한자리씩 주어지는 건줄 모르고 판단을 어떻게 해야 하는가 고민했는데
예제를 보니까 한자리 숫자만 주어지는 것 같아서 한 자리 숫자 기준으로 코드를 짰더니 맞았다.
'''