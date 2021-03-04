from src.data_structure.linkedList.model import ListNode


# https://leetcode.com/problems/palindrome-linked-list/
class Solution234:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        # test 1,2,1 and 1,1
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_head = slow.next
        slow.next = None
        new_head = self.reverse(new_head)

        while head and new_head:
            if head.val != new_head.val: return False
            head = head.next
            new_head = new_head.next

        return True

    def reverse(self, head):
        prev, curr = None, head
        while curr:
            ncurr = curr.next
            curr.next = prev
            prev = curr
            curr = ncurr

        return prev
