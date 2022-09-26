#11399. ATM
#문제 링크 : https://www.acmicpc.net/problem/11399

#내 풀이 - 책 가이드 보고
import sys

n=int(sys.stdin.readline())
nums=list(map(int, input().split()))

for i in range(1, n):
    idx=i
    num=nums[i]
    for j in range(0, i):
        if nums[i]<nums[j]:
            idx=j
            break
    for k in range(i, idx, -1):
        nums[k]=nums[k-1]
    nums[idx]=num

            


output=0
for i in range(n):
    output+=sum(nums[0:i+1])

print(output)

'''
처음 코드 짰을 때는 삽입이 아니라 두 값 위치를 교환을 해버렸다.
책을 다시 보니까 삽입위치부터 index 위치까지 shift 연산을 수행해야한다고 해서
하나씩 옮기는 부분(for k 부분)은 책을 참고해서 짰다.
'''