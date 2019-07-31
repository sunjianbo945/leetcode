from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        no_block = True
        for i in range(m - 1, -1, -1):
            if no_block:
                if obstacleGrid[i][-1] == 1:
                    dp[i][-1] = 0
                    no_block = False
                    continue
                dp[i][-1] = 1
            else:
                dp[i][-1] = 0

        no_block = True
        for i in range(n - 1, -1, -1):
            if no_block:
                if obstacleGrid[-1][i] == 1:
                    dp[-1][i] = 0
                    no_block = False
                    continue
                dp[-1][i] = 1
            else:
                dp[-1][i] = 0

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


def main():
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))


if __name__=='__main__':
    main()