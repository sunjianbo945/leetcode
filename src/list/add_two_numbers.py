
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Add_Two_Numbers_2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        extra = 0
        head = ListNode(0)
        temp = head

        while l1 and l2:
            if l1.val + l2.val + extra < 10:
                temp.next = ListNode(l1.val + l2.val + extra)
                extra = 0
            else:
                temp.next = ListNode(l1.val + l2.val + extra - 10)
                extra = 1

            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        node = l1 if l1 else l2

        while node:
            if node.val + extra < 10:
                temp.next = ListNode(node.val + extra)
                extra = 0
            else:
                temp.next = ListNode(node.val + extra - 10)
                extra = 1

            temp = temp.next
            node = node.next

        if extra > 0:
            temp.next = ListNode(extra)

        return head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Add_Two_Numbers_II_445:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q1 = []
        q2 = []

        while l1:
            q1.append(l1.val)
            l1 = l1.next

        while l2:
            q2.append(l2.val)
            l2 = l2.next

        q = []

        extra = 0
        while len(q1) and len(q2):
            n1 = q1.pop()
            n2 = q2.pop()
            if n1 + n2 + extra < 10:
                q.append(n1 + n2 + extra)
                extra = 0
            else:
                q.append(n1 + n2 + extra - 10)
                extra = 1

        non_empty_q = q1 if len(q1) else q2

        while len(non_empty_q):
            n = non_empty_q.pop()
            if n + extra < 10:
                q.append(n + extra)
                extra = 0
            else:
                q.append(n + extra - 10)
                extra = 1

        if extra > 0:
            q.append(extra)

        head = ListNode(0)
        temp = head
        while len(q):
            temp.next = ListNode(q.pop())
            temp = temp.next

        return head.next





