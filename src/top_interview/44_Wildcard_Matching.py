class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(1, len(dp[0])):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in range(1, len(dp)):

            for j in range(1, len(dp[0])):

                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == '*':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]
