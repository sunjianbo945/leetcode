from heapq import *
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        heap = []
        for start, end in intervals:
            heappush(heap, (start, end))

        s, e = heappop(heap)

        while heap:
            if e > heap[0][0]: return False
            s, e = heappop(heap)

        return True