from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memo = {}

        for i in range(len(nums)):

            ans = target - nums[i]

            if ans in memo:
                return [memo[ans], i]
            else:
                memo[nums[i]] = i

        return []