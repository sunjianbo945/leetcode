from typing import List


# https://leetcode.com/problems/task-scheduler/
class Solution621:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)