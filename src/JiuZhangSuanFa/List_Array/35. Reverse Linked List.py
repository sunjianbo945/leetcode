"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next




class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here

        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cur = head
        pre = dummy
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        dummy.next = pre
        head.next = None
        return dummy.next