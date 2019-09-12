from typing import List
import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        head = ListNode(0)
        q = PriorityQueue()
        for idx,node in enumerate(lists):
            q.put((node.val, idx, node))

        temp = head
        while q:
            _, idx, node = q.get()
            temp.next = node
            temp = temp.next
            node = node.next
            if node:
                q.put((node.val,idx, node))
        return head.next


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


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
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            lists = stringToListNodeArray(line)

            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print
            out
        except StopIteration:
            break


if __name__ == '__main__':
    main()