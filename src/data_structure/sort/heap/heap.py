from collections import *
from heapq import *
from typing import List

from src.data_structure.linkedList.model import ListNode


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


# https://leetcode.com/problems/reorganize-string/
class Solution767:
    def reorganizeString(self, S: str) -> str:
        char_count = Counter(S)
        heap = []

        for char, count in char_count.items():
            heappush(heap, (-count, char))

        res = []
        while len(heap) >= 2:
            n1, c1 = heappop(heap)
            n2, c2 = heappop(heap)

            res.append(c1)
            res.append(c2)

            if n1 + 1 < 0: heappush(heap, (n1 + 1, c1))
            if n2 + 1 < 0: heappush(heap, (n2 + 1, c2))

        if len(heap) == 1:
            if heap[0][0] == -1:
                res.append(heap[0][1])
            else:
                return ''

        return ''.join(res)


# https://leetcode.com/problems/merge-k-sorted-lists/
class Solution23:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(heap, (node.val, i, node))

        dummy = ListNode(-1)
        cur = dummy

        while heap:
            _, k, node = heappop(heap)
            cur.next = node
            cur = node
            if node.next:
                heappush(heap, (node.next.val, k, node.next))

        return dummy.next


# https://leetcode.com/problems/ipo/
class Solution502:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))

        n = len(Profits)
        projects = [(Capital[i], Profits[i]) for i in range(n)]
        projects.sort(key=lambda x: x[0], reverse=True)

        available = []
        while k > 0:
            while projects and projects[-1][0] <= W:
                capital, profit = projects.pop()
                heappush(available, -profit)  # max heap

            if available:
                W -= heappop(available)
            else:
                break
            k -= 1
        return W


# https://leetcode.com/problems/most-profit-assigning-work/
class Solution826:
    def maxProfitAssignment(self, d: List[int], p: List[int], worker: List[int]) -> int:
        max_profit = []
        for diff, profit in zip(d, p):
            heappush(max_profit, (-profit, diff))  # max profit heap

        res = 0
        for w_d in sorted(worker, reverse=True):
            while max_profit and w_d < max_profit[0][1]:
                heappop(max_profit)

            res -= max_profit[0][0] if max_profit else 0

        return res


# https://leetcode.com/problems/trapping-rain-water-ii/
class Solution407:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        seen = set()
        m, n = len(heightMap), len(heightMap[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        heap = []
        for i in range(n):
            seen.add((0, i))
            seen.add((m - 1, i))
            heappush(heap, (heightMap[0][i], 0, i))
            heappush(heap, (heightMap[m - 1][i], m - 1, i))

        for i in range(1, m - 1):
            seen.add((i, 0))
            seen.add((i, n - 1))
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))

        round_min = 0
        res = 0
        while heap:
            h, x, y = heappop(heap)
            round_min = max(round_min, h)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen: continue

                seen.add((nx, ny))
                diff = round_min - heightMap[nx][ny]
                res += diff if diff > 0 else 0
                heappush(heap, (heightMap[nx][ny], nx, ny))

        return res


# https://leetcode.com/problems/campus-bikes/
class Solution1057:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []

        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))

            # Sort the tuples
        distances.sort()

        result = [-1] * len(workers)
        bike_taken = set()  # Mark a bike as taken by putting it in this set as we traverse the tuples from shortest distance onwards.
        for distance, i, j in distances:
            # print(distance, i, j)
            if result[i] == -1 and j not in bike_taken:
                result[i] = j
                bike_taken.add(j)
        return result


# https://leetcode.com/problems/high-five/
class Solution1086:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_score = defaultdict(list)

        for curr_id, score in items:
            scores = id_score[curr_id]
            heappush(scores, score)

            if len(scores) > 5:
                heappop(scores)

        res = []
        for curr_id in sorted(id_score):
            res.append([curr_id, int(sum(id_score[curr_id]) / 5)])

        return res


# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
class Solution1167:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1: return 0
        heap = []
        for stick in sticks:
            heappush(heap, stick)

        res = 0
        while len(heap) > 1:
            n1 = heappop(heap)
            n2 = heappop(heap)
            res += n1 + n2
            heappush(heap, n1 + n2)

        return res

