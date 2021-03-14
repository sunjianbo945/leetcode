from math import inf
from typing import List


# https://leetcode.com/problems/maximum-subarray/
# dp[i] is the max sum subarray ending at i. so dp[i] = max(A[i], A[i] + dp[i-1])
class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_ending_i = -inf
        global_sum = -inf

        for i in range(len(nums)):
            max_sum_ending_i = max(nums[i], max_sum_ending_i + nums[i])
            global_sum = max(global_sum, max_sum_ending_i)

        return global_sum

    def maxSubArray_rewrite(self, nums: List[int]) -> int:
        curMax, maxSum = -inf, -inf

        for i in range(len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            global_sum = max(maxSum, curMax)

        return maxSum


# https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution918:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)

            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)

            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
