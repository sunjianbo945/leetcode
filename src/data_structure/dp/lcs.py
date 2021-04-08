from functools import lru_cache

# https://leetcode.com/problems/longest-common-subsequence/
from math import inf


class Solution1143:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def dfs(i, j):
            if i == m or j == n: return 0

            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)

            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)

    def longestCommonSubsequence_dp(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for col in reversed(range(n)):
            for row in reversed(range(m)):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]

    def longestCommonSubsequence_sequence(self, text1: str, text2: str) -> str:
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def dfs(i, j):
            if i == m or j == n: return ''

            if text1[i] == text2[j]:
                return text1[i] + dfs(i + 1, j + 1)

            l = dfs(i + 1, j)
            r = dfs(i, j + 1)

            return l if len(l) > len(r) else r

        return dfs(0, 0)

    def longestCommonSubsequence_sequence_dp(self, text1: str, text2: str) -> str:
        m, n = len(text1), len(text2)
        dp = [[''] * (n + 1) for _ in range(m + 1)]

        for col in reversed(range(n)):
            for row in reversed(range(m)):
                if text2[col] == text1[row]:
                    dp[row][col] = text1[row] + dp[row + 1][col + 1]
                else:
                    if len(dp[row + 1][col]) > len(dp[row][col + 1]):
                        dp[row][col] = dp[row + 1][col]
                    else:
                        dp[row][col] = dp[row][col + 1]

        return dp[0][0]


# https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/
class Solution:
    def longestCommonSubarry(self, A, B):
        m, n = len(A), len(B)
        res_len, res = -inf, []
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] += 1 + dp[i + 1][j + 1]
                    if dp[i][j] > res_len:
                        res_len = dp[i][j]
                        res = A[i:i + dp[i][j]]
                        
        return res


if __name__ == '__main__':
    # https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/
    A = [1, 2, 8, 2, 1]
    B = [8, 2, 1, 4, 7]
    print(Solution().longestCommonSubarry(A, B))
