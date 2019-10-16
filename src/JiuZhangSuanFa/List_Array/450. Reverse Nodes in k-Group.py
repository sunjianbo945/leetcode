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
    @param k: An integer
    @return: a ListNode
    """

    def reverseKGroup(self, head, k):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre:
            pre = self.reverseKNodes(pre, k)

        return dummy.next

    def reverseKNodes(self, pre_node, num):
        # n1,n2 .... nk,nk+1
        node = pre_node
        for _ in range(num):
            node = node.next
            if not node:
                return
        nk = node
        nk_plus_one = node.next

        # start to reverse
        # pre->[n1->n2..nk]->nk+1
        cur = pre_node.next
        n1 = pre_node.next
        pre = pre_node
        for _ in range(num):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        pre_node.next = nk
        n1.next = nk_plus_one

        return n1