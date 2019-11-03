from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height or len(height) == 1: return 0

        left, right = 0, len(height) - 1
        left_height, right_height = height[0], height[-1]
        total = 0

        while left < right:

            h = min(left_height, right_height)

            if left_height <= right_height:
                total += max(0, h - height[left])
                left += 1
                left_height = max(left_height, height[left])
            else:
                total += max(0, h - height[right])
                right -= 1
                right_height = max(right_height, height[right])

        return total
