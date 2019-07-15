# leetcode link
# Difficulty: ***
# DFS

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        self.dfs_helper(sorted(nums), [], ans, len(nums), used)
        return ans

    def dfs_helper(self, nums: List[int], cur: List[int], result: List[int], length: int, used_flag: List[bool]):

        if len(cur) == length:
            result.append(cur)
            return

        for i in range(len(nums)):
            if used_flag[i]:
                continue
            if i > 0 and used_flag[i - 1] and nums[i] == nums[i - 1]:
                continue
            used_flag[i] = True
            self.dfs_helper(nums, cur + [nums[i]], result, length, used_flag)
            used_flag[i] = False


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs_helper(sorted(nums), [], ans, len(nums))
        return ans

    def dfs_helper(self, nums: List[int], cur: List[int], result: List[int], length: int):

        if len(cur) == length:
            result.append(cur)
            return

        prev = None
        for index, value in enumerate(nums):
            if prev == value:
                continue
            prev = value
            self.dfs_helper(nums[:index] + nums[index + 1:], cur + [nums[index]], result, length)


def main():
    print(Solution().permuteUnique([1,2,3]))
    print(Solution2().permuteUnique([1,2,3]))


if __name__=='__main__':
    main()