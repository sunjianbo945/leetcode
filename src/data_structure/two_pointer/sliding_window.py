from math import inf
from typing import List


# https://leetcode.com/problems/subarray-product-less-than-k/
class Solution713:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        pre_prod = 1
        res = 0
        for r in range(n):
            pre_prod *= nums[r]

            while pre_prod >= k and l <= r:
                pre_prod /= nums[l]
                l += 1

            res += r - l + 1  # logic outside

        return res


# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution209:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        n = len(pre_sum)
        l = 0
        res = inf
        for r in range(n):
            curr = pre_sum[r] - pre_sum[l]

            while curr >= k and l < r:
                res = min(res, r - l)  # logic inside
                l += 1
                curr = pre_sum[r] - pre_sum[l]

        return res if res < inf else 0
