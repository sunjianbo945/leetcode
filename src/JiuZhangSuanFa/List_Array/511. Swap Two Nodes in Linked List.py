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
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        # write your code here
        if not head: return

        dummy = ListNode(0)
        dummy.next = head

        pre1, cur1 = self.find_node(dummy, v1)
        pre2, cur2 = self.find_node(dummy, v2)

        if not pre1 or not cur1 or not pre2 or not cur2:
            return dummy.next

        pre1.next = cur2
        temp = cur2.next

        if pre2 == cur1:
            cur2.next = cur1
            cur1.next = temp
        else:
            cur2.next = cur1.next
            pre2.next = cur1
            cur1.next = temp

        return dummy.next

    def find_node(self, dummy, val):

        cur = dummy.next
        pre = dummy
        while cur:
            if cur.val == val:
                return pre, cur

            cur = cur.next
            pre = pre.next

        return None, None