# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from heapq import heappush, heappop
from typing import List


class KthLargest703:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []  # store the largest k numbers
        self.max_heap = []  # store the first k smaller numbers
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.max_heap, -val)
        val = -heappop(self.max_heap)
        heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heappush(self.max_heap, -heappop(self.min_heap))

        return self.min_heap[0]
