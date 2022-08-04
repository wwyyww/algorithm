#17298. 오큰수
#문제 링크 : https://www.acmicpc.net/problem/17298

#내 풀이 - 시간초과
import sys
n=int(sys.stdin.readline())
strs=sys.stdin.readline().rstrip().split(' ')
nums = [int(x) for x in strs]

for i in range(0, n):
    j=i+1
    if j>n-1:
        print(-1)
        break
    while j<n:
        if nums[i]<nums[j]:
            print(nums[j])
            break
        else:
            j+=1
    if j<n:
        continue
    else:
        print(-1)

'''
반복문을 사용해서 풀었기 때문에 시간초과로 실패했다.
'''

#다른 풀이
#참고 : https://codingspooning.tistory.com/entry/BOJ-%EB%B0%B1%EC%A4%80-17298%EB%B2%88-%EC%98%A4%ED%81%B0%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
n=int(sys.stdin.readline())
strs=sys.stdin.readline().rstrip().split(' ')
nums = [int(x) for x in strs]
output=[-1]*n
stack=[]

for i in range(0, n):
    while stack and nums[stack[-1]] < nums[i]:
        output[stack.pop()]=nums[i]
    stack.append(i)

print(*output)

'''
스택을 사용해서 푼다.
스택에는 인덱스 값이 들어간다.
while문은 stack에 값이 있으면서 nums에서 기준 인덱스를 기준으로 오른쪽에 큰 값이 있다면 output의 값이 -1에서 변경된다.
nums 값이 [9, 5, 4, 8]일때 5는 처음에 4와 먼저 비교되기 때문에 output[1]의 값은 -1 이다가
반복문이 진행되면서 8까지 오게되면 5보다 큰 값을 만나기 때문에 outpu[1]의 값은 8로 바뀌게 된다.
'''