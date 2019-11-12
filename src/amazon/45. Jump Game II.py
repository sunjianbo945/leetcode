from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        further_pos = 0
        cur_end = 0
        jump = 0

        for i in range(len(nums) - 1):

            if i + nums[i] > further_pos: further_pos = i + nums[i]

            if i == cur_end:
                jump += 1
                cur_end = further_pos

        return jump


