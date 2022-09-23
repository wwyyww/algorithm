#1377. 버블 소트
#문제 링크 : https://www.acmicpc.net/problem/1377

#내 풀이 - 책 가이드라인 보고

nums=list(input())
n=len(nums)
for i in range(n):
    max=i
    for j in range(i+1, n):
        if nums[max]<nums[j]:
            max=j
    nums[max], nums[i]=nums[i], nums[max]


print("".join(nums))

'''
책 가이드라인을 보고 max 값을 인덱스로 설정하고 인덱스 기준으로 최댓값에 접근했다.
인덱스를 활용하는 습관을 길러보자..
'''