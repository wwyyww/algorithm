#242. Valid Anagram
#문제 링크 : https://leetcode.com/problems/valid-anagram/

#내 풀이

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if sorted(list(s))==sorted(list(t)):
            return True
        return False

'''
파이썬에서 기본으로 제공하는 정렬함수를 사용해서 비교했다.
'''


#책 풀이
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

'''
나랑 같은 방식인데 return에 조건을 넣어서 한 줄로 끝냈다.
'''