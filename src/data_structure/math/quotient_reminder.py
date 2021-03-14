from collections import defaultdict
from typing import List


# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
class Solution1010:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_count = defaultdict(int)
        res = 0
        for t in time:
            t %= 60

            res += time_count[0] if not t else time_count[60 - t]

            time_count[t] += 1

        return res


# https://leetcode.com/problems/continuous-subarray-sum/
# a%k = x
# b%k = x
# (a - b) %k = x -x = 0
# here a - b = the sum between i and j.
class Solution523:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum_idx = defaultdict()
        pre_sum_idx[0] = -1
        pre_sum = 0
        for idx, num in enumerate(nums):
            pre_sum += num
            if k != 0:
                pre_sum %= k

            if pre_sum in pre_sum_idx:
                if idx - pre_sum_idx[pre_sum] > 1:
                    return True
            else:
                pre_sum_idx[pre_sum] = idx

        return False
