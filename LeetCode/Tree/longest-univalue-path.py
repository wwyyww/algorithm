#687. Longest Univalue Path
#문제 링크 : https://leetcode.com/problems/longest-univalue-path/

#책 풀이 : DFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result

'''
탐색은 무조건 진행하고 상태값 업데이트는 조건을 확인하고 업데이트를 한다.  
(나는 그냥 탐색자체를 조건을 만족하면 진행하는 코드를 생각했다.)
값이 부모 노드와 같은 경우에만 거리를 증가시킨다. 
결과는 result와 좌우 자식노드 거리의 합을 합친 것의 최대값으로 갱신한다. 
상태값을 반환할 때는 자식 중에 더 큰 값의 상태를 반환한다.
'''