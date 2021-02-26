# Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i]
# is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left
# of the rectangular cake to the jth vertical cut.
#
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts
# and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.
#

from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontal_boundary, vertical_boundary = [0] + horizontalCuts + [h], [0] + verticalCuts + [w]

        h_max_diff, v_max_diff = float('-inf'), float('-inf')

        for i in range(len(horizontal_boundary) - 1):
            h_max_diff = max(horizontal_boundary[i + 1] - horizontal_boundary[i], h_max_diff)

        for i in range(len(vertical_boundary) - 1):
            v_max_diff = max(vertical_boundary[i + 1] - vertical_boundary[i], v_max_diff)

        return (h_max_diff * v_max_diff) % (10 ** 9 + 7)
