#208. Implement Trie (Prefix Tree)
#문제 링크 : https://leetcode.com/problems/implement-trie-prefix-tree/

#책 풀이
import collections


# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

'''
트라이 노드를 따로 TrieNode로 빼서 구현했다. word는 단어 여부를 확인하기 위한 속성이고 
children은 해당 노드의 자식 노드들을 딕셔너리 형태로 저장한다.

insert 구현
주어진 단어의 각 문자들을 노드의 children으로 삽입한다. 
만약 단어를 다 넣으면 마지막 노드의 word 속성을 True로 바꿔준다. 

search 구현
주어진 단어가 노드의 자식에 없다면 False를 반환하고 있다면 탐색을 계속하고 끝까지 가면 True를 반환한다.

startsWith 구현
해당 문자가 노드의 자식에 없다면 False를 반환하고 만약 모든 문자들이 다 있다면 True를 반환한다.
'''