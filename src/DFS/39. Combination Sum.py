from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), 0, target, [], res)
        return res

    def dfs(self, candidates, position, target, cur, res):

        if target == 0:
            res.append(cur)
            return

        for i in range(position, len(candidates)):
            if candidates[i] > target:
                break
            self.dfs(candidates, i, target - candidates[i], cur + [candidates[i]], res)