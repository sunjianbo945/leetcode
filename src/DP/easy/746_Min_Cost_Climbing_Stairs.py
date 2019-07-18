from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 0:
            return 0

        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        # print(dp)
        return min(dp[0], dp[1])


def main():
    print(Solution().minCostClimbingStairs([2, 0, 3, 5, 2, 1]))


if __name__=='__main__':
    main()