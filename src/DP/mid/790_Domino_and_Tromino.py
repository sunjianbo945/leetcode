

# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-790-domino-and-tromino-tiling/

# dp[i][0], i fully filled
# dp[i][1], i fully filled with additional upper half
# dp[i][2], i fully filled with additional bottom half


class Solution:
    def numTilings(self, N):
        mod = 10 ** 9 + 7
        dp = [[0, 1, 2] for _ in range(N+1)]
        dp[0][0], dp[0][1], dp[0][2] = 1, 0, 0
        dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1
        for i in range(2, N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod
        return dp[N][0]