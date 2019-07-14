# leetcode link
# Difficulty: ***
# DFS

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs_helper(nums, [], ans)
        return ans

    def dfs_helper(self, nums: List[int], cur: List[int], result: List[List[int]]):

        result.append(cur)

        if len(nums) == 0:
            return

        for i in range(len(nums)):
            self.dfs_helper(nums[i + 1:], cur + [nums[i]], result)

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for i in range(len(nums)):
            for j in range(len(ret)):
                ret.append(ret[j] + [nums[i]])

        return ret


def main():
    print(Solution().subsets([1,2,3]))

if __name__=='__main__':
    main()
