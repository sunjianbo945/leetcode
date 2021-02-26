import heapq
from typing import *


# Given allLocations list of co-ordinates (x,y) you have to find the X - closest locations from truck's location which is (0,0). Distance is calculated using formula (x^2 + y^2).
# If the there is tie then choose the co-ordinate with least x value.
# Sample Input :
# allLocations : [ [1, 2] , [1, -1], [3, 4] ]
# numOfDeliveries : 2
# Sample Output :
# [ [1, -1], [1 , 2] ]
# Output list can be in any order.
# This question was basically K closest points to the origin (0,0) with added tie condition.
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
