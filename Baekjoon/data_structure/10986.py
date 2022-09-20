#10986. 나머지 합
#문제 링크 : https://www.acmicpc.net/problem/10986

#내 풀이
import sys
from collections import Counter
first=sys.stdin.readline
n, m=map(int, first().split())
nums=list(map(int, input().split()))
sums=[]
output=0
tmp=0
for num in nums:
    tmp=tmp+num
    sums.append(tmp%m)

count=Counter(sums)
for key, value in count.items():
    if key==0:
        output+=value*(value-1)//2+value
    elif value>1:
        output+=value*(value-1)//2
print(output)

'''
책에 적혀있는 흐름을 보고 구현했다.
구간 합 배열은 구간 합에 나머지 연산을 한 값으로 구성한다.
나머지 연산의 값이 0인 경우는 그 개수만큼 결과값에 더하고
나머지가 같은 인덱스의 개수가 2개 이상이면 경우의 수를 구해서 결과값에 더한다.
이때 나머지가 0인 경우도 포함이 된다.
'''