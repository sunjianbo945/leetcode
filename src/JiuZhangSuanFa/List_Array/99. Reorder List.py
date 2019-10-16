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
    @param head: The head of linked list.
    @return: nothing
    """

    def reorderList(self, head):
        # write your code here
        if not head or not head.next: return head

        mid = self.find_mid(head)

        second_head = self.reverse(mid.next)

        mid.next = None

        cur = head
        # 1->2->3->null
        # 5->4->null
        # cur = 1
        while second_head:
            temp = cur.next  # temp = 2
            cur.next = second_head  # 1->5
            cur = cur.next  # cur = 5
            second_head = second_head.next  # second_head = 4
            cur.next = temp  # 5->2
            cur = cur.next  # cur = 2

        return head

    def find_mid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
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