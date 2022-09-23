#1377. 버블 소트
#문제 링크 : https://www.acmicpc.net/problem/1377

#내 풀이 - 시간초과
import sys

n=int(sys.stdin.readline())

nums=[]
for _ in range(n):
    now=int(sys.stdin.readline())
    nums.append(now)

for i in range(n):
    change=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            change=True
            nums[j], nums[j+1]=nums[j+1], nums[j]
    if not change:
        print(i+1)
        break


#책 풀이
import sys

n=int(sys.stdin.readline())

nums=[]
for i in range(n):
    now=int(sys.stdin.readline())
    nums.append((now, i))

sort_nums=sorted(nums)

max=0
for i in range(n):
    if max<sort_nums[i][1]-i:
        max=sort_nums[i][1]-i

print(max+1)

'''
나는 그냥 주어진 코드를 파이썬으로 변환하기만 하면 되는 줄 알았는데 
시간초과가 떠서 다르게 풀어야 되는구나 싶었는데 어떻게 풀어야 될 지 모르겠어서 책을 봤다.
근데 책에서 정렬 전 인덱스 - 정렬 후 인덱스의 최댓값을 구해야 한다고 해서
처음에는 왜 최댓값을 구해야 하는 건지 이해가 안갔다.
정렬 전 인덱스 - 정렬 후 인덱스의 최댓값의 의미는 버블 정렬을
최댓값만큼만 하면 정렬이 된다는 뜻이다. 
따라서 최댓값을 구하면 그 이후에는 swap이 일어나지 않기 때문에 최댓값+1을 print하면 된다.
'''