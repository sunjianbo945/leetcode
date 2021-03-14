from collections import defaultdict

from src.data_structure.linkedList.model import ListNode, NodeWithRadom


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


# https://leetcode.com/problems/copy-list-with-random-pointer/
class Solution138:
    def copyRandomList(self, head: 'NodeWithRadom') -> 'NodeWithRadom':
        if not head: return None
        curr = head
        node_copied = defaultdict()
        while curr:
            node_copied[curr] = NodeWithRadom(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copied = node_copied[curr]
            copied.next = node_copied[curr.next] if curr.next else None
            copied.random = node_copied[curr.random] if curr.random else None
            curr = curr.next
        return node_copied[head]

    def copyRandomList_itervative(self, head: 'NodeWithRadom') -> 'NodeWithRadom':
        if not head: return None
        curr = head
        # create copy in the list
        while curr:
            curr.next = NodeWithRadom(curr.val, curr.next)
            curr = curr.next.next
        # link random
        prev, curr = head, head.next
        while prev:
            curr.random = prev.random.next if prev.random else None
            prev = curr.next
            curr = prev.next if prev else None

        # split
        dummy = NodeWithRadom(-1)
        prev, curr = head, head.next
        dummy.next = curr
        while prev:
            prev.next = curr.next
            curr.next = curr.next.next if curr.next else None
            prev = prev.next
            curr = curr.next

        return dummy.next
