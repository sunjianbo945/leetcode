# this works when the range of value in the array is small. this is use when range is small but the n is big
from typing import List


# https://leetcode.com/problems/two-sum-less-than-k/
class Solution1099:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:  # O(range), O(range)
        res = -1
        count = [0] * 1001
        for num in nums:  # counting sort
            count[num] += 1
        l, r = 0, len(count) - 1
        while l < r:
            while l < r and count[l] == 0:
                l += 1

            while l < r and count[r] == 0:
                r -= 1

            if l == r and count[l] < 2: break  # check has enough number to user

            curr = l + r
            if curr < k:
                l += 1
                res = max(res, curr)
            else:
                r -= 1
        return res
