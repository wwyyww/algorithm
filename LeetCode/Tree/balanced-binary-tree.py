#110. Balanced Binary Tree
#문제 링크 : https://leetcode.com/problems/balanced-binary-tree/

#책 풀이 : 재귀
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or \
                    right == -1 or \
                    abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1

'''
재귀 호출로 맨 아래 노드까지 내려가면 해당 노드는 left, right 모두 0을 반환한다. 
두 노드의 높이 차이가 크지 않으면 둘 중 최댓값에 1을 더한 값을 반환한다. 
그렇게 점점 위로 갈수록 1씩 증가한다. 
만약 높이 차이가 1을 넘으면 -1을 리턴하고 한번 -1이 나오면 계속 -1을 반환한다. 
그래서 최종 결과로 -1과의 일치여부를 확인한다. -1이면 False고 -1이 아니면 True가 나온다.

나는 책처럼 각 노드의 높이를 확인하고 비교하려고 하지 않고 최소 높이를 찾아서 차이를
비교하려고 했는데 최소 높이를 찾는 방식을 잘못 생각해서 자꾸 틀린 경우가 나왔다.

'''