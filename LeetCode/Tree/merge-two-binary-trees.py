#617. Merge Two Binary Trees
#문제 링크 : https://leetcode.com/problems/merge-two-binary-trees/

#책 풀이 : 재귀

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2

'''
주어진 함수를 수정해서 그 함수를 재귀 호출하는 방식이다. 함수는 노드를 반환한다. 
만약 두 노드다 값이 있으면 값을 더하고 해당 노드의 자식들까지 함수를 재귀호출해서 병합한다. 
노드 중 하나만 값이 있으면 값이 있는 노드만 반환을 한다.

내가 시도했던 풀이를 생각해보면 함수가 어떤 걸 반환할지를 잘못 생각했다. 
책처럼 노드를 반환하면 잘 해결되는건데 값을 반환하려고 하니까 뭔가 복잡해진 것 같다.
그리고 책 풀이에서 return t1 or t2 부분 진짜 간단하게 해결했는데 나는 이렇게 생각 못했다.
'''