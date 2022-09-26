#11004. K번째 수
#문제 링크 : https://www.acmicpc.net/problem/11004

#책 풀이
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:  # K번째 수가 pivot이면 더이상 구할 필요 없음
            return
        elif K < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)
        else:  # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K)


def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(S, E):
    global A

    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E

    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E
    while i <= j:
        while pivot < A[j] and j > 0:
            j = j - 1
        while pivot > A[i] and i < len(A)-1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j


quickSort(0, N - 1, K - 1)
print(A[K - 1])


#퀵 정렬 구현 다른 방식 - 인터넷
#출처 : https://freedeveloper.tistory.com/377

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)



'''
퀵 정렬.. 복잡하다..
'''