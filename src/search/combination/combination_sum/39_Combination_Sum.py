# leetcode link
# Difficulty: ***
# https://leetcode.com/problems/combination-sum/
# DFS

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        ans = []
        self.dfs_helper(sorted(candidates), [], target, ans)
        return ans

    def dfs_helper(self, candidates: List[int], cur: List[int], target: int, result: List[List[int]]):

        if target == 0:
            result.append(cur)
            return

        for i in range(len(candidates)):
            if candidates[i] > target: # this part will short the time, so it must to be sorted at the beginning
                break
            self.dfs_helper(candidates[i:], cur + [candidates[i]], target - candidates[i], result)


def main():
    print(Solution().combinationSum([2,3,6,7],7))

if __name__=='__main__':
    main()