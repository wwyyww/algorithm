#17298. 오등큰수
#문제 링크 : https://www.acmicpc.net/problem/17299

#내 풀이
import sys
from collections import Counter

n=int(sys.stdin.readline())
strs=sys.stdin.readline().rstrip().split(' ')
nums = [int(x) for x in strs]
count=Counter(nums)
output=[-1]*n
stack=[]

for i in range(0, n):
    while stack and count[nums[stack[-1]]]<count[nums[i]]:
        output[stack.pop()]=nums[i]
    stack.append(i)

print(*output)

'''
17298과 다른 점은 횟수를 비교하는 것이기 때문에 Counter 객체를 사용해서 풀었다.
코드 구조는 17298과 같다.
'''