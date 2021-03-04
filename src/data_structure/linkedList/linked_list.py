from src.data_structure.linkedList.model import ListNode


# https://leetcode.com/problems/reverse-linked-list/
class Solution206:
    def reverseList_dfs(self, head: ListNode) -> ListNode:
        if not head: return None

        def dfs(node):
            nonlocal head
            if not node.next:
                head = node
                return node

            prev = dfs(node.next)
            prev.next = node

            return node

        last = dfs(head)
        last.next = None
        return head

    def reverseList_stack(self, head: ListNode) -> ListNode:
        if not head: return None
        stack = []

        while head:
            stack.append(head)
            head = head.next

        head = stack.pop()
        curr = head
        while stack:
            curr.next = stack[-1]
            curr = stack.pop()

        curr.next = None
        return head

    def reverseList_iterative(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            ncurr = curr.next
            curr.next = prev
            prev = curr
            curr = ncurr

        return prev


# https://leetcode.com/problems/add-two-numbers-ii/
class Solution445:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next
            n1 += 1
        while curr2:
            curr2 = curr2.next
            n2 += 1

        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        if n1 > n2:
            curr1, curr2 = l1, l2
        else:
            curr1, curr2 = l2, l1
            n1, n2 = n2, n1

        curr = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 > n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            else:
                val += curr2.val + curr1.val
                curr1 = curr1.next
                curr2 = curr2.next
                n1 -= 1
                n2 -= 1

            # update the result: add to front
            prev = ListNode(val, curr)
            curr = prev

        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, curr = curr, None
        carry = 0
        while curr1:
            carry, val = divmod(curr1.val + carry, 10)
            # update the result: add to front
            prev = ListNode(val, curr)
            curr = prev

            # move to the next elements in the list
            curr1 = curr1.next

        # add the last carry
        if carry:
            pre = ListNode(carry, curr)
            curr = pre

        return curr
