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
