#297. Serialize and Deserialize Binary Tree
#문제 링크 : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

#책 풀이
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

'''
이진트리 구조는 논리적인 구조라서 파일에 저장할 때는 물리적인 형태로 변환해야 한다. 
이를 직렬화라고 하고 반대는 역직렬화다. 파이썬에는 pickle이라는 직렬화 모듈이 있다. 

책에서는 BFS 탐색 결과로 직렬화를 한다. 빈 공간은 #으로 표현한다. 
join할 때 공백을 넣기 때문에 각 노드마다 구분이 된다. 
그렇기 때문에 역질렬화를 할 때 공백단위로 문자열을 끊어서 nodes 리스트로 만든다. 
자식 노드의 결과를 먼저 확인하고 인덱스 값을 증가시킨다.
'''