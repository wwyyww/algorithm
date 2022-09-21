#1940. 주몽 
#문제 링크 : https://www.acmicpc.net/problem/1940

#내 풀이

import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

nums=list(map(int, input().split()))
nums.sort()

start=0
end=n-1
output=0
sum=nums[end]+nums[start]
while start<end:
    if sum==m:
        output+=1
        sum-=nums[end]+nums[start]
        end-=1
        start+=1
        sum+=nums[end]+nums[start]
    elif sum>m:
        sum-=nums[end]
        end-=1
        sum+=nums[end]
        
    else:
        sum-=nums[start]
        start+=1
        sum+=nums[start]
        
print(output)

'''
책에서는 그냥 sum 변수를 안 사용하고 nums[end]+nums[start]를 조건식에 사용해서
코드가 더 간단하다.
'''

