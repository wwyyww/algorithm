#5. Longest Palindromic Substring
#문제 링크 : https://leetcode.com/problems/longest-palindromic-substring/

#내 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==1:
            return s
        
        output=''
        
        def check(start, end, text):
            while start>=0 and end<len(s):
                tmp=text[start:end+1]
                if tmp==tmp[::-1]:
                    start-=1
                    end+=1
                else:
                    break
            
            return text[start+1:end]

        
        for i in range(len(s)):
            
            string=check(i, i, s)
            if len(string)>len(output):
                output=string
            
            string=check(i, i+1, s)
            if len(string)>len(output):
                output=string
        
        return output
            
        
'''
다른 사람 풀이를 참고해서 풀었다.
for 문에서는 팰린드롬 문자열의 길이가 짝수인 경우와 홀수인 경우를 위해 확인을 2번했다.
'''


#책 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result

'''
우선 주어진 글자가 한글자거나 전체가 팰린드롬인 경우는 먼저 처리한다.

끝 글자가 같다면 포인터를 확장하는 함수인 expand 함수를 정의한다.

expand 함수에서 return할 때 left+1을 한 이유
⇒ 만약에 팰린드롬이면 포인터가 확장되는데 확장되고 나서 조건에 해당하지 않으면 
다시 이전 문자열로 가야하기 때문에 left+1을 해줘야 한다. right은 원래 인덱싱 끝부분은 -1이라서 따로 처리하지 않은 것이다.

포인터는 짝수, 홀수 모든 경우를 판별하기 위해 expand 함수를 두번 사용했다. 
max 함수에 key=len을 설정해서 길이를 기준으로 최댓값을 반환한다.
'''