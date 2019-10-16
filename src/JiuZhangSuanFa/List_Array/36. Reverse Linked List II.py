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
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head:return

        if m==n:
            return head

        dummy = ListNode(0)
        dummy.next = head


        pre = self._get_pre_node(dummy,m)

        self.reverse(pre,n-m)

        return dummy.next

    def _get_pre_node(self, dummy, m):

        cur = dummy.next
        pre = dummy
        for _ in range(m-1):
            cur = cur.next
            pre = pre.next


        return pre


    def reverse(self, pre_node, num):
        # n1,n2,nm-1->[nm ->,,->nn]->nn+1
        dummy = pre_node
        head= dummy.next

        cur = dummy.next
        pre = dummy
        for _ in range(num+1):
            if not cur: return
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        nn = pre
        nn_plus_one = cur
        dummy.next = nn
        head.next = nn_plus_one