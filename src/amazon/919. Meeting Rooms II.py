"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals = sorted(intervals, key=lambda x: x.start)

        heap = []

        for i in range(len(intervals)):

            if heap and intervals[i].start > heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i].end)

        return len(heap)



