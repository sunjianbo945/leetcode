import json
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head: return None

        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next

        loop = 1
        dummy = ListNode(0)
        dummy.next = head

        while loop < size:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = self.split(l, loop)
                cur = self.split(r, loop)

                m_head, m_tail = self.merge(l, r)
                tail.next = m_head
                tail = m_tail

            loop += loop

        return dummy.next

    def split(self, node, size):

        if not node: return None
        pre = node
        while size and node:
            size -= 1
            pre = node
            node = node.next

        pre.next = None
        return node

    # return the head and the tail of the to pointers
    def merge(self, left, right):

        if not left and not right: return (None, None)

        head = ListNode(0)

        temp = head

        while left and right:

            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next

            temp = temp.next

        if not left:
            temp.next = right
        else:
            temp.next = left

        while temp.next:
            temp = temp.next

        tail = temp
        return (head.next, tail)


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().sortList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()