#148. Sort List
#문제 링크 : https://leetcode.com/problems/sort-list/

#내 풀이

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        node=head
        nums=[]
        while node:
            nums.append(node.val)
            node=node.next
        
        nums.sort()
        node=head
        for num in nums:
            node.val=num
            node=node.next
        
        return head

'''
버블정렬을 사용해서 풀었는데 시간초과가 나오길래 일단 문제를 풀기위해서
파이썬 내장함수 sort를 사용해서 풀었다.
'''

#책 풀이 : 런너 기법을 활용한 병합정렬

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 두 정렬 리스트 병합
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

'''
병합정렬이기 때문에 분할하는 함수, 합치는 함수를 구현한다.
분할 함수 : sortList
연결리스트의 길이를 알 수 없기 때문에 런너 기법을 사용한다.
slow는 한칸씩, fast는 두칸씩 이동한다. fast가 끝까지 가면 slow는 중앙에 도달한다.
half는 slow 이전 값이고 처음~half, slow~끝 으로 분할을 한다.
분할된 리스트를 인자로 재귀호출을 한다. 그러면 결국 하나의 값으로 쪼개지게 된다.

합치는 함수 : mergeTwoLists
쪼개진 값들을 합칠 때 크기를 비교한 후에 다음 값들을 연결한다.
'''
