import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.index = 0

    def addNum(self, num: int) -> None:
        self.index += 1

        heapq.heappush(self.max_heap, (-num, self.index))

        max_half, index = heapq.heappop(self.max_heap)

        heapq.heappush(self.min_heap, (-max_half, index))

        if len(self.min_heap) > len(self.max_heap):
            min_half, index = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_half, index))

    def findMedian(self) -> float:

        if len(self.min_heap) != len(self.max_heap):
            return -self.max_heap[0][0]

        else:
            return (-self.max_heap[0][0] + self.min_heap[0][0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()