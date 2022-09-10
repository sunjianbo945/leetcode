from heapq import *
from typing import List


# https://leetcode.com/problems/-rooms/
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


'''
Facebook interview
Given a set of meetings defined by [start_time, end_time] find out max number of meetings we can accommodate (i.e. w/o 
overlap among the meetings) using one meeting room.
Example Input:
meeting1 [0, 30]
meeting2 [5, 10]
meeting3 [15, 20]
Example Output: 2
'''

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        end_time_heap = []  # number of end times in this heap represent the needed room number
        room_required = 0
        for start_time, end_time in sorted_intervals:
            while end_time_heap and start_time >= end_time_heap[0]:  # meetings with any ending time before current start time already ended, should be poped out.
                heapq.heappop(end_time_heap)
            heapq.heappush(end_time_heap, end_time)
            room_required = max(room_required, len(end_time_heap))
        return room_required
