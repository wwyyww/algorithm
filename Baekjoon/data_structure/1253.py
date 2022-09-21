#1253. 좋다 
#문제 링크 : https://www.acmicpc.net/problem/1253

#내 풀이 - 실패
import sys
n=int(sys.stdin.readline())
nums=list(map(int, input().split()))
nums.sort()

start=0
end=n-2
target=n
good=[]

for i in range(n):
    target-=1
    end=n-1
    start=0

    if target==0:
        start=1

    while start<end:
        if end==target:
            end-=1
            continue

        if nums[start]+nums[end]==nums[target]:
            good.append(nums[target])
            break
        
        elif nums[start]+nums[end]<nums[target]:
            start+=1

        else:
            end-=1

print(len(good))

#책 풀이
import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()
for k in range(N):
    find = A[k]
    i = int(0)
    j = int(N - 1)
    while i < j:  # 투 포인터 알고리즘
        if A[i] + A[j] == find:  # find는 서로 다른 두 수의 합 이어야 함을 체크
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
print(Result)

'''
거의 다 된 것 같은데 자꾸 틀렸길래 너무 오래 잡고 있었다....
결국 책을 봤는데 되게 단순한데 내가 생각을 잘못했다.
우선 초반에 시도할 때는 for문을 안쓰고 while문 하나로 해결하려고 조건이 더 복잡해졌다.
그래서 책을 살짝 보니까 for문이랑 while문을 같이 쓰길래 그렇게 바꿨는데
조건을 또 잘못 세워서 자꾸 틀렸다.

생각해보면 그냥 더한 값이 같을 때 포인터의 값을 확인하면 되는데
왜 미리 확인하려고 했는지 모르겠다..
'''