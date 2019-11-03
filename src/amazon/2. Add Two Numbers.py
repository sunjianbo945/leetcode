from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 or not l2:
            return l1 if not l2 else l2

        extra = 0
        dummy = ListNode(0)
        temp = dummy

        while l1 and l2:

            if l1.val + l2.val + extra >= 10:

                temp.next = ListNode(l1.val + l2.val + extra - 10)
                extra = 1
            else:
                temp.next = ListNode(l1.val + l2.val + extra)
                extra = 0

            l1 = l1.next
            l2 = l2.next
            temp = temp.next

        l1 = l1 if not l2 else l2

        while l1:

            if l1.val + extra >= 10:
                temp.next = ListNode(l1.val + extra - 10)
                extra = 1
            else:
                temp.next = ListNode(l1.val + extra)
                extra = 0

            l1 = l1.next
            temp = temp.next

        if extra == 1:
            temp.next = ListNode(1)

        return dummy.next
