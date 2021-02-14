from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, res,set())
        return res

    def dfs(self, nums, start, res, dup):

        if start == len(nums):
            res.append(list(nums))
            return

        for i in range(start, len(nums)):
            if nums[i] in dup:
                continue
            dup.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            self.dfs(nums, start+1, res,dup)
            nums[start], nums[i] = nums[i], nums[start]
            dup.remove(nums[i])


print(Solution().permuteUnique([2,2,1,1]))

