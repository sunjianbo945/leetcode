"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        # copy node
        self.copyNode(head)
        # build random relationship
        self.build_random(head)
        # break nodes

        return self.breakNode(head)

    def copyNode(self, head):

        cur = head

        while cur:
            newNode = Node(cur.val, cur.next, None)
            cur.next = newNode
            cur = newNode.next

    def build_random(self, head):

        cur = head
        newNode = head.next

        while cur:
            newNode.random = cur.random.next if cur.random else None
            cur = newNode.next
            if cur:
                newNode = cur.next

    def breakNode(self, head):
        dummy = Node(-1, None, None)

        cur = head
        newNode = head.next

        dummy.next = newNode

        while cur:
            cur.next = newNode.next
            newNode.next = cur.next.next if cur.next else None

            cur = cur.next
            newNode = cur.next if cur else None

        return dummy.next






class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head is None:
            return None

        table = {}

        temp = head
        while temp is not None:
            table[temp.val] = Node(temp.val, None, None)
            temp = temp.next

        temp = head
        while temp is not None:
            table[temp.val].next = table[temp.next.val] if temp.next is not None else None
            table[temp.val].random = table[temp.random.val] if temp.random is not None else None
            temp = temp.next

        return table[head.val]