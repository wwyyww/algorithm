#11689. GCD(n, k) = 1
#문제 링크 : https://www.acmicpc.net/problem/11689

#내가 시도한 풀이 - 실패
import sys
import math

n=int(sys.stdin.readline())
n=int(math.sqrt(n))

nums=list(0 for _ in range(n))
check=list(0 for _ in range(n))

for i in range(n):
    nums[i]=i+1
    check[i]=i+1

for i in range(1, n):
    if check[i]==i+1:
        for j in range(i, n, i):
            check[j]=check[j]-check[j]/(i+1)

print(check[n-1])


#책 풀이

import sys
import math

n=int(sys.stdin.readline())

check=n

for i in range(2, int(math.sqrt(n))+1):
    if n%i==0:
        check-=check/i
        while n%i==0:
            n/=i

if n>1:
    check-=check/n

print(int(check))

'''
나는 앞에 설명된 오일러 피 함수 설명을 보고 리스트를 다 생성했는데 굳이 그럴 필요가 없었다. 
이 문제는 하나의 수에 대해서 소인수의 개수를 구하면 되기 때문에 그 원리를 활용해서 코드를 짜면 된다.

우선 탐색 범위는 소수인 2부터 입력 값의 제곱근까지다.
만약 n이 i의 배수라면 결과값을 업데이트한다.
그 다음에 n에서 i를 없애기 위해 i로 안나눠질때까지 n을 업데이트한다.

반복문을 다 진행한 후에 n>1 부분은 종료 범위가 제곱근이라서 소인수가 누락되는 경우를 위한 부분이다.
예를 들어서 주어진 숫자가 10이라면 탐색 종료 범위가 4이기 때문에 5는 누락된다.

'''