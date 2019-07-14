# leetcode link
# Difficulty: ***
# DFS

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs_helper(sorted(nums) ,0, [] ,ans)
        return ans

    def dfs_helper(self, nums :List[int], start :int, cur :List[int], result :List[int]):

        result.append(cur)

        if len(nums )==0:
            return

        for i in range(start, len(nums)):
            if i> start and nums[i] == nums[i - 1]:
                continue
            self.dfs_helper(nums, i + 1, cur + [nums[i]], result)



def main():
    print(Solution().subsetsWithDup([1,2,2]))

if __name__=='__main__':
    main()
