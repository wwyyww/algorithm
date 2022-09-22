#1874. 스택 수열
#문제 링크 : https://www.acmicpc.net/problem/1874

#내 풀이
import sys

n=int(sys.stdin.readline())
stack=[]
output=[]
i=0
no=False

for _ in range(n):
    now=int(sys.stdin.readline())
    while True:
        if stack and stack[-1]>now:
            no=True
            break
        if not stack or stack[-1]<now:
            i+=1
            stack.append(i)
            output.append('+')
        if stack[-1]==now:
            stack.pop()
            output.append('-')
            break


if no:
    print('NO')
else:
    for out in output:
        print(out)

'''
책에서는 출력 값을 문자열로 만들어서 줄바꿈까지 추가해서 출력할 때 나처럼 반복문을 사용하지 않았다.
'''