# leetcode link
# Difficulty: ***
# DFS

from typing import List



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs_helper(n, 1, k, [], ans)
        return ans

    def dfs_helper(self, n: int, start: int, k: int, cur: List[int], result: List[List[int]]):

        if k == 0:
            result.append(cur)
            return

        for i in range(start, n + 1):
            self.dfs_helper(n, i + 1, k - 1, cur + [i], result)


def main():
    print(Solution().combine(8,3))

if __name__=='__main__':
    main()