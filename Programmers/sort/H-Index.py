#42747. H-Index
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42747

#내 풀이

def solution(citations):
    sort_citations = sorted(citations, reverse=True)
    
    for idx, item in enumerate(sort_citations):
        if idx >= item:
            return idx
    
    return len(sort_citations)

'''
1. 주어진 인용횟수 배열을 내림차순으로 정렬한다.
2. 인덱스 값이 인용횟수보다 크거나 같을 때, 해당 인덱스가 h-index가 된다.
3. 만약 모든 논문의 인용횟수가 인덱스보다 큰 경우에는 배열의 길이가 h-index가 된다.
'''