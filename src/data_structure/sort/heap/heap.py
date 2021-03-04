from collections import *
from heapq import *
from typing import List


# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution973:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:  # O(nlogk), O(k)
        heap = []  # max heap
        for x, y in points:
            dis = x * x + y * y
            heappush(heap, (-dis, x, y))

            if len(heap) > K:
                heappop(heap)

        return [[x, y] for ids, x, y in heap]


# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution215:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # min heap
        for x in nums:
            heappush(heap, x)

            if len(heap) > k:
                heappop(heap)

        return heappop(heap)


# https://leetcode.com/problems/third-maximum-number/
class Solution414:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []  # min heap
        for x in set(nums):
            heappush(heap, x)

            if len(heap) > 3:
                heappop(heap)

        return heappop(heap) if len(heap) >= 3 else max(heap)


# https://leetcode.com/problems/top-k-frequent-elements/
class Solution347:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # O(nlogk) O(n)
        nums_count = Counter(nums)
        heap = []  # min heap
        for num, count in nums_count.items():

            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)

        return [num for count, num in heap]


class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count > other.count:
            return False
        else:
            return self.word > other.word


# https://leetcode.com/problems/top-k-frequent-words/
class Solution692:  # customize heap comparison
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        heap = []

        for word, count in word_count.items():
            heappush(heap, Node(count, word))

            if len(heap) > k: heappop(heap)

        return [heappop(heap).word for _ in range(len(heap))][::-1]


# https://leetcode.com/problems/kth-largest-element-in-a-stream/
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


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


# https://leetcode.com/problems/employee-free-time/
class Solution759:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        for emp in schedule:
            for iv in emp:
                heap.append((iv.start, iv.end))
        heapify(heap)

        s, e = heappop(heap)
        free = e
        res = []
        while heap:
            s, e = heappop(heap)
            if s > free:
                res.append(Interval(free, s))
                free = e
            else:
                free = max(free, e)
        return res
