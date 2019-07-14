# leetcode link
# Difficulty: ***
# https://leetcode.com/problems/combination-sum-ii/
# DFS

from typing import List,Tuple,Set


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        ans = []
        self.dfs_helper(sorted(candidates), 0, [], target, ans)
        return ans

    def dfs_helper(self, candidates: List[int], start, cur, target: int, result: List[List[int]]):

        if target == 0:
            result.append(cur)
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:  # this part will short the time, so it must to be sorted at the beginning
                break

            if i > start and candidates[i] == candidates[i - 1]:
                continue

            self.dfs_helper(candidates, i + 1, cur + [candidates[i]], target - candidates[i], result)


def main():
    print(Solution().combinationSum2([10,1,2,7,6,1,5],8))


if __name__=='__main__':
    main()