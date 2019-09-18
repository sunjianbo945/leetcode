from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        heappush(self.l, -1 * num)
        val = heappop(self.l)
        heappush(self.r, -1 * val)
        if len(self.l) < len(self.r):
            val = heappop(self.r)
            heappush(self.l, -1 * val)

    def findMedian(self) -> float:

        if len(self.l) > len(self.r):
            return -1*self.l[0]
        else:
            return (-1*self.l[0] + self.r[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.findMedian()
obj.addNum(3)
obj.findMedian()
param_2 = obj.findMedian()