#11659. 구간 합 구하기 4 
#문제 링크 : https://www.acmicpc.net/problem/11659

#내 풀이 - 시간초과 실패
first=list(map(int, input().split()))
nums=list(map(int, input().split()))
sums=[0]
for i in range(0, first[0]):
    if i==0:
        sums.append(nums[i])
    else:
        sums.append(sums[i]+nums[i])

for i in range(first[1]):
    section=list(map(int, input().split()))
    print(sums[section[1]]-sums[section[0]-1])

#책 풀이
import sys
input = sys.stdin.readline
suNo,quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prifix_sum = [0]
temp = 0
for i in numbers:
    temp = temp + i
    prifix_sum.append(temp)
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prifix_sum[e]-prifix_sum[s-1])

'''
내가 푼 풀이는 시간초과로 실패했다.
책에서는 readline으로 받고 구간합 리스트를 만들때 리스트 인덱스에 접근하지 않고
for문으로 numbers의 숫자에 접근했다.
값을 접근할 때 리스트 인덱스로 접근하는 것은 피하는 게 좋겠다.
'''