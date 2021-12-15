# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curi = head
        while curi:
            curj = curi.next
            while curj:
                if curi.val > curj.val:
                    tmp = curi.val
                    curi.val = curj.val
                    curj.val = tmp
                curj = curj.next
            curi = curi.next
        return head