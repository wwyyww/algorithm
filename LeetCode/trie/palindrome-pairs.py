#336. Palindrome Pairs
#문제 링크 : https://leetcode.com/problems/palindrome-pairs/

#내 풀이 (시간초과)
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        output=[]
        
        for idx, word in enumerate(words):
            for idx2, word2 in enumerate(words):
                if idx==idx2:
                    continue
                if word+word2==(word+word2)[::-1]:
                    output.append([idx, idx2])
        
        return output

#책 풀이 : 트라이 구현
import collections
from typing import List


# 트라이 저장할 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직 3) (본문 설명 참고)
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 1) (본문 설명 참고)
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직 2) (본문 설명 참고)
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

'''
모든 입력값을 뒤집어서 트라이를 구성한다. (근데 왜 뒤집어서 구성? 팰린드롬 확인할 때 편하려고?)
해당 입력값의 인덱스를 알아야 하기 때문에 인덱스를 저장한다. 
*판별로직 1 : 끝까지 탐색했을 때 word_id가 있는 경우
입력값을 탐색하다가 끝나는 지점의 word_id 값이 -1이 아니고 
입력값의 index와 다르면 팰린드롬으로 판별할 수 있다.

*판별로직 2 : 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
트라이를 삽입할 때 단어자체가 팰린드롬이면 미리 팰린드롬 여부를 세팅하는 것이다.
insert할 때 단어에서 문자 수를 줄이면서 팰린드롬 여부를 확인한다.(is_palindrome)
이때 문자 하나도 팰린드롬이기 때문에 팰린드롬 여부가 세팅된다.
palindrome_word_ids에 팰린드롬으로 판별된 인덱스가 저장된다.

*판별로직 3 : 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
입력값을 순서대로 확인하다가 해당 노드의 word_id가 -1이 아닌 경우
나머지 문자가 팰린드롬이면 팰린드롬으로 판별한다.




'''        