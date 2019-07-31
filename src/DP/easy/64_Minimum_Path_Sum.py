from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]

        for i in range(n - 2, -1, -1):
            dp[-1][i] = dp[-1][i + 1] + grid[-1][i]

        for i in range(m - 2, -1, -1):
            dp[i][-1] = dp[i + 1][-1] + grid[i][-1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]

        return dp[0][0]


def main():
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


if __name__=='__main__':
    main()