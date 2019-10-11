from typing import *


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        res = []
        self.recur(nums, [], res)
        return res

    def recur(self, nums, cur: List[int], res: List[List[int]]):

        if not nums:
            res.append(cur)
            return

        for i in range(len(nums)):
            self.recur(nums[:i] + nums[i + 1:], cur + [nums[i]], res)