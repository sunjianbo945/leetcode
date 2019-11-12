from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_time_can_jump = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_time_can_jump:
                last_time_can_jump = i

        return last_time_can_jump == 0
