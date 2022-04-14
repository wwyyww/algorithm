#424. Longest Repeating Character Replacement
#문제 링크 : https://leetcode.com/problems/longest-repeating-character-replacement/

#책 풀이
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=right=0
        counts=collections.Counter()
        for right in range(1, len(s)+1):
            counts[s[right-1]]+=1
            #가장 흔하게 등장하는 문자 탐색
            max_char_n=counts.most_common(1)[0][1]

            #k 초과시 왼쪽 포인터 이동
            if right-left-max_char_n>k:
                counts[s[left]]-=1
                left+=1
        return right-left

'''
오른쪽 포인터에서 왼쪽 포인터 위치를 뺀 후 윈도우 안에서 출현 빈도가 가장 높은 문자의 수를
뺀 값이 k와 같을 수 있는 수가 최댓값이라 할 수 있다.
AAABB에서 A를 B로 바꾸는건 3번, B를 A로 바꾸는  건 2번의 연산이 필요하다.
오른쪽 포인터 5에서 0을 빼고 출현빈도가 높은 A의 수 3을 빼면 2가 된다.
그게 k와 같아지면서 결과 값은 2가 된다.
최대 길이가 되는 값은 오른쪽 포인터에서 왼쪽 포인터를 뺀 값이다.
'''