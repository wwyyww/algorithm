#2018. 수들의 합 5
#문제 링크 : https://www.acmicpc.net/problem/2018

#내 풀이

import sys

n=int(sys.stdin.readline())
start, end=1, 1
output=0
tmp=0

while start<=n:
    if tmp>=n:
        tmp=0
        start, end=start+1, start+1
    elif tmp<n:
        tmp+=end
        if tmp==n:
            output+=1
        end+=1

print(output)


#책 풀이
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1
while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
print(count)
        
'''
투 포인터를 사용해서 풀었다.
근데 나는 python3로 하면 시간초과가 나서 pypy3로 바꿔서 제출했는데
책 풀이는 시간초과가 안난다.
이유를 찾아보자. 이것저것 바꿔서 시도해본 결과 내가 생각하기에는
내 코드에서 조건식에서 tmp=0으로 바꾸는게 문제였던 것 같다.
아예 그런 방식이 아니라 책 처럼 인덱스를 더하거나 빼는 방식으로 합을 구하는
방식으로 해야 시간초과가 안나는 것 같다.
책에 방식에서는 1은 더해지지 않아서 합에 1을 미리 더해두고 시작하고 
마지막에 n과 같은 수만 더하는 경우도 미리 count 값이 더하고 시작한다.
'''
    