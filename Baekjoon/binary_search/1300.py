#1300. K번째 수
#문제 링크 : https://www.acmicpc.net/problem/1300

#책 풀이

import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
start=1
end=k
output=0

while start<=end:
    mid=int((start+end)/2)
    cnt=0

    for i in range(1, n+1):
        cnt+=min(int(mid/i), n)
    if cnt<k:
        start=mid+1
    else:
        output=mid
        end=mid-1
        

print(output)

'''
진짜 이런 방법은 어떻게 생각하는 건지..
정답은 작은 수의 개수가 k-1개인 중앙값이다.
중앙값보다 작거나 같은 수의 개수를 세는 방법은 중앙값을 n으로 나눈 값이다.
작거나 같은 수의 개수를 확인하면서 k와 같거나 커지는 경우에 답을 업데이트한다.
'''

