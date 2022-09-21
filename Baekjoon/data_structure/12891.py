#12891. DNA 비밀번호
#문제 링크 : https://www.acmicpc.net/problem/12891

#내 풀이 - 시간초과 실패

import sys
from collections import Counter


s, p = map(int, sys.stdin.readline().split())
dna=sys.stdin.readline()
a, c, g, t=map(int, sys.stdin.readline().split())
count=Counter({'A':a, 'C':c, 'G':g, 'T':t})
start=0
end=p
output=0

for _ in range(s-p+1):
    tmp=dna[start:end]
    cnt=Counter(tmp)

    if len(count-cnt)==0:
        output+=1

    start+=1
    end+=1

print(output)


#책 풀이
checkArr = [0] * 4
myArr = [0] * 4
checkSecret = 0

# 함수 정의
def myadd(c): #새로 들어온 문자를 처리하는 함수
    global checkArr,myArr,checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

def myremove(c): #제거되는 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkArr = list(map(int, input().split()))
for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1
for i in range(P):  #초기 P 부분 문자열 처리 부분
    myadd(A[i])
if checkSecret == 4: #4자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    Result += 1
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1
print(Result)


'''
Counter를 써서 그런지 내 풀이는 시간초과로 실패했다.
책에서는 Counter를 안쓰고 슬라이딩 윈도우만 사용한다.
슬라이딩 윈도우를 옮기면서 추가되는 문자, 빠지는 문자에 따라 
함수를 생성하고 조건을 만족하는지 확인하는 함수도 있다.
함수를 만들었기 때문에 추가되고 없어지는 문자만 반영해서 조건 여부를 확인할 수 있다.
'''