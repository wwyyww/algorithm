#108. Convert Sorted Array to Binary Search Tree
#문제 링크 : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#실패
#책 풀이 : 이진 검색 결과로 트리 구성

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

'''
반으로 쪼갠후에 좌, 우를 나눠서 재귀 호출로 처리를 한다.
굉장히 간단하게 처리가 된다. 나도 시도할 때 root의 중간값을 사용하긴 했는데 탐색과정을
너무 하나하나 생각한 것 같다.
그냥 계속 절반씩 나눠서 인덱스의 중앙값을 찾아서 트리를 구성하면 된다.

'''