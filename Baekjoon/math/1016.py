#1016. 제곱 ㄴㄴ 수
#문제 링크 : https://www.acmicpc.net/problem/1016

#내 풀이 - 실패

'''
import sys

min, max = map(int, sys.stdin.readline())
output=0
nums=[0 for _ in range(min, max+1)]

start=1
base=2

while base**2<max:
    square=base**2
    for i in range(start, max):
        i=start*square
        if (i*min-1)%square==0:
            nums[i]

1. 제곱수로 범위 내의 수 모두 나누기
- 나눌수가 제곱수보다 작으면 무조건 패스 => 제곱수가 max보다 크면 다음 제곱수로 안가기


1-1. 나눠지면 output에 추가하고 추후에 나눌 범위에서 제외시키기
1-2. 안나눠지면 패스

문제 : 이미 제곱 ㄴㄴ 수가 아닌 수를 또 셀 수도 있음 => 리스트로 표시하기

'''


#책 풀이
import sys
import math

min, max = map(int, sys.stdin.readline().split())
nums=[0 for _ in range(max-min+1)]
output=0

for i in range(2, int(math.sqrt(max))+1):  # 반복문(1)
    square=i**2
    start=int(min/square)
    if min%square!=0: start+=1
    for j in range(start, int(max/square)+1): # 반복문(2)
        nums[j*square-min]=-1

for i in range(0, max-min+1):
    if nums[i]==0:
        output+=1
    
print(output)


'''
책 풀이 : 에라토스테네스의 체 알고리즘 방식을 적용한 방식

모든 수들을 탐색하지 않고 제곱수의 배수인 수를 탐색하는 방식으로 진행한다.

반복문(1)에서 종료 범위를 max의 제곱근으로 지정했기 때문에 이중 반복문을 사용해도 시간 초과가 발생하지 않는다.
종료 범위를 max로 한 경우에는 시간 초과가 발생한다.

start 변수가 int(min/square)인 이유는 제곱수보다 작은 수는 탐색하지 않기 위해서다.
반복문(2)에서 종료 범위가 int(max/square)+1인 이유는 max보다 작은 범위의 제곱수를 탐색하기 위해서다.

'''