#76. Minimum Window Substring
#문제 링크 : https://leetcode.com/problems/minimum-window-substring/

#책 풀이 - 1 : 투 포인터, 슬라이딩 윈도우
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]

'''
슬라이딩 윈도우면서 적절한 위치에서 좌우 포인터를 줄이는 방식이다.
need는 필요한 문자의 개수를 Counter 객체로 저장한다.
오른쪽 포인터인 right 값은 계속 증가시킨다. 
만약 현재 문자가 필요한 문자에 포함되어 있다면 필요문자 개수를 감소시키고 해당 필요문자의 개수도 감소시킨다.

필요문자가 0이면 왼쪽 포인터를 줄일 수 있는지 확인한다.
불필요한 문자라면 음수이기 때문에 0인 곳까지 왼쪽 포인터를 움직인다.
더 작은 윈도우 값이 나타나면 start, end를 갱신한다.
'''
