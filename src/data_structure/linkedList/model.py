class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeWithRadom:
    def __init__(self, x: int, next: 'NodeWithRadom' = None, random: 'NodeWithRadom' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import contextvars

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        print('reverlise head local = ')
        print(locals())
        def dfs(node):
            global head
            print('global')
            print(dict(globals()))
            print('local')
            print(dict(locals()))

            print("### node:", node.val, "  head:", head.val)
            if not node.next:
                head = node
                print('global')
                print(dict(globals()))
                print('local')
                print(dict(locals()))
                return head
            prev = dfs(node.next)
            prev.next = node
            print("$$$ node:", node.val, "  head:", head.val)
            print(dict(globals()))
            return node

        last = dfs(head)
        last.next = None
        print('final local = ')
        print(locals())
        print('final global = ')
        print(globals())
        print("@@@ head:", head.val, "last:", last.val)
        return head


head = Solution().reverseList(head)

cur = head
while cur:
    print(cur.val)
    cur = cur.next
