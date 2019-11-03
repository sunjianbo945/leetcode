import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):

            x, y = points[i]
            dis = x * x + y * y

            heapq.heappush(heap, (-dis, i, points[i]))

            if len(heap) > K:
                heapq.heappop(heap)

        return [i[2] for i in heap]
