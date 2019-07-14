# leetcode link
# Difficulty: ***
# DFS

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        used = [False] * len(nums)
        self.dfs_helper(nums, [], ans, len(nums), used)
        return ans

    def dfs_helper(self, nums: List[int], cur: List[int], result: List[int], length: int, used_flag: List[bool]):

        if len(cur) == length:
            result.append(cur)
            return

        for i in range(len(nums)):
            if used_flag[i]:
                continue
            used_flag[i] = True
            self.dfs_helper(nums, cur + [nums[i]], result, length, used_flag)
            used_flag[i] = False

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        self.dfs_helper(nums, [], ans, len(nums))
        return ans

    def dfs_helper(self, nums: List[int], cur: List[int], result: List[int], length: int):

        if len(cur) == length:
            result.append(cur)
            return

        for i in range(len(nums)):
            self.dfs_helper(nums[:i] + nums[i + 1:], cur + [nums[i]], result, length)


def main():
    print(Solution().permute([1,2,3]))
    print(Solution2().permute([1,2,3]))


if __name__=='__main__':
    main()
