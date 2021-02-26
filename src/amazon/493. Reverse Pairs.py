# 493. Reverse Pairs
# Hard
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
# Note:
#
#     The length of the given array will not exceed 50,000.
#     All the numbers in the input array are in the range of 32-bit integer.


from typing import *

from sortedcontainers import SortedList


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        left = SortedList()
        res = 0
        for num in nums:
            target = num * 2
            # print(num, target, left, res)

            res += len(left) - left.bisect_right(target)
            left.add(num)

        return res


# but amazon asked
# Number of Swaps to Sort
# Given an array and a sorting algorithm, the sorting algorithm will do a selection swap. Find the number of swaps to sort the array.
# Sample input:
# [5,4,1,2] -> pair (5,4) -> [4,5,1,2] -> pair (4,1) -> [1,5,4,2] -> pair(5,4) -> [1,4,5,2] -> pair(4,2) -> [1,2,5,4] -> pair(5,4) -> [1,2,4,5].
# I was able to solve 9/14 test cases using O^2 time complexity. I first thought it was to figure out the min num of swaps to do it then realized it was different. Ran out of time trying to solve the correct problem.
# Sample output:
# Return 5
import bisect


class Solution:
    def reversePairsAmazon(self, nums: List[int]) -> int:
        left = []
        res = 0
        for num in nums:
            target = num
            # print(num, target, left, res)
            idx = bisect.bisect_right(left, target)
            res += len(left) - idx
            left.insert(idx, num)

        return res


print(Solution().reversePairsAmazon([5, 4, 1, 2]))
