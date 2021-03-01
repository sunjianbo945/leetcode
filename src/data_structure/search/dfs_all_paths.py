from functools import lru_cache
from typing import *


# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution797:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:  # O(2^n*n) O(n)
        seen = set()
        curr = [0]
        n = len(graph)
        res = []

        def dfs(node):
            if node == n - 1:
                res.append(list(curr))
                return

            seen.add(node)
            for neighbor in graph[node]:
                if neighbor in seen: continue

                curr.append(neighbor)
                dfs(neighbor)
                curr.pop()  # backtrack

            seen.remove(node)  # backtrack

        dfs(0)
        return res

    def allPathsSourceTarget_cache(self, graph: List[List[int]]) -> List[List[int]]:
        seen = set()
        n = len(graph)

        @lru_cache(None)
        def dfs(node):
            if node == n - 1:
                return [[node]]

            res = []
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor in seen: continue

                for path in dfs(neighbor):  # path can be [1,2]
                    res += [node] + path

            seen.remove(node)  # backtrack
            return res

        return dfs(0)


# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
class Solution1155:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # the number of possible ways

        @lru_cache(None)
        def dfs(d, target):
            if target <= 0: return 0
            if d == 1:
                if 0 < target <= f: return 1
                return 0

            res = 0
            for i in range(1, f + 1):
                res += dfs(d - 1, target - i)

            return res % (10 ** 9 + 7)

        return dfs(d, target)

# https://leetcode.com/problems/permutations/
class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]: # O(n!)
        n = len(nums)
        res = []

        def dfs(idx):
            if idx >= n:
                res.append(list(nums))
                return

            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]  # backtrack

        dfs(0)
        return res
