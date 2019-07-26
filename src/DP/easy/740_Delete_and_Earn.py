import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c = collections.Counter(nums)
        memo = sorted([(i,v) for i,v in c.items()])
        dp = [0 for _ in range(len(memo))]
        dp[0] = memo[0][1] * memo[0][0]
        for i in range(1, len(memo)):
            dp[i] = memo[i][1] * memo[i][0]
            if memo[i][0] == memo[i - 1][0] + 1:
                if i != 1:
                    dp[i] += dp[i - 2]
                dp[i] = max(dp[i], dp[i - 1])
            else:
                dp[i] += dp[i - 1]
        return dp[-1]



def main():
    print(Solution().deleteAndEarn([2, 0, 3, 5, 2, 1]))


if __name__=='__main__':
    main()