#147. Insertion Sort List
#문제 링크 : https://leetcode.com/problems/insertion-sort-list/

#내 풀이 : 미완성
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        root=head
        node=head.next
        
        
        while node:
            while root.val>node.val:
                if root.val > node.val:
                    root.val, node.val=node.val, root.val
                root=head.next
            node=node.next
                
            
        
        return head
        
'''
형태가 연결리스트여서 삽입해야 할 노드를 연결리스트의 끝부분에서 앞쪽으로 탐색하는 과정을
어떻게 구현할지가 어려웠다.

'''

#책 풀이 : 삽입 정렬의 비교 조건 개선
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next

'''
정렬할 대상과 정렬된 대상을 나눠서 진행한다. 
head : 정렬대상, cur : 정렬 완료
cur의 첫 노드는 초기값이기 때문에 cur.next.val과 head.val을 비교한다.
정렬을 해야 하는 위치를 찾으면 cur.next에 head를 연결하고 head.next로 cur.next를 해서
이어주고 head는 다음 head로 넘어가기 위해 head.next를 한다. 
성능을 개선하기 위해 cur이 head보다 클때만 cur이 처음으로 돌아가게 한다.

'''