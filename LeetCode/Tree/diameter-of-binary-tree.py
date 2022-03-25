#543. Diameter of Binary Tree
#문제 링크 : https://leetcode.com/problems/diameter-of-binary-tree/

#책 풀이 : 상태값 누적 트리 DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest
'''
가장 긴 경로를 찾기 위해서는 가장 밑의 노드까지 탐색하고 부모로 거슬러 가면서 거리를 계산하면 된다. 
탐색을 하는데 만약 해당 노드에 자식 노드가 없으면 없는 노드에 상태 값을 -1로 반환한다. 

가장 긴 경로는 지금까지 가장 긴 경로, 왼쪽 자식과 오른쪽 자식의 상태값에 2를 더한 값의 최댓값을 비교해서 갱신한다. 

dfs는 상태값을 반환하는 함수이기 때문에 return 값은 상태값을 의미한다. longest가 경로의 길이를 저장하는 변수다. 
longest 변수를 함수 안에서 정의하지 않고 클래스 변수로 선언을 했다. 그래서 함수 안에서는 self.longest로 사용한다. 
이렇게 사용한 이유는 숫자가 불변객체라 중첩 함수 내에서는 값을 변경할 수 없기 때문이다.
'''