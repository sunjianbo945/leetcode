from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists: return
        array = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(array, (lists[i].val, i, lists[i]))

        dummy = ListNode(-1)
        temp = dummy
        while array:

            val, index, node = heapq.heappop(array)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(array, (node.next.val, index, node.next))

        return dummy.next