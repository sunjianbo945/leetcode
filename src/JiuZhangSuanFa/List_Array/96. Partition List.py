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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if not head: return

        dummy_less_x = ListNode(0)
        dummy_greater_x = ListNode(0)
        temp_less_x = dummy_less_x
        temp_greater_x = dummy_greater_x

        cur = head

        while cur:
            if cur.val < x:
                temp_less_x.next = cur
                temp_less_x = temp_less_x.next
            else:
                temp_greater_x.next = cur
                temp_greater_x = temp_greater_x.next

            cur = cur.next

        temp_greater_x.next = None
        temp_less_x.next = dummy_greater_x.next

        return dummy_less_x.next