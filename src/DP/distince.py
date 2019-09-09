class Minimum_ASCII_Delete_Sum_for_Two_Strings_712:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for i in range((len(s1) + 1))]

        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])

        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[-1][-1]


class Delete_Operation_for_Two_Strings_583:
    def minDistance(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s2)+1) for i in range((len(s1)+1))]

        for i in range(1,len(dp[0])):
            dp[0][i] = dp[0][i-1]+1

        for i in range(1,len(dp)):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1)

        return dp[-1][-1]


class Distinct_Subsequences_115:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for i in range((len(t) + 1))]

        for i in range(len(dp[0])):
            dp[0][i] = 1

        for i in range(1, len(dp)):
            for j in range(i, len(dp[0])):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]
