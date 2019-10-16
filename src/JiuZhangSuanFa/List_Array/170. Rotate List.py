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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        # write your code here
        if not head: return
        total = self.count(head)
        k = k % total

        if k == 0: return head

        dummy = ListNode(0)
        dummy.next = head

        pre_node, last_node = self.find_last_node(dummy, k)
        if dummy == pre_node:
            return dummy.next

        dummy.next = pre_node.next
        last_node.next = head
        pre_node.next = None
        return dummy.next

    def count(self, head):
        count = 0

        while head:
            count += 1
            head = head.next

        return count

    def find_last_node(self, head, k):
        cur = head
        for _ in range(k):
            cur = cur.next
            if not cur: break

        slow = head
        while cur and cur.next:
            cur = cur.next
            slow = slow.next

        return slow, cur