#  [LintCode] 533 Two Sum - Closest to target 解题报告
# Description
# Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
#
# Return the difference between the sum of the two integers and the target.
#
#
#
# Example
# Given array nums = [-1, 2, 1, -4], and target = 4.
#
# The minimum difference is 1. (4 - (2 + 1) = 1).
#
#
#
# Challenge
# Do it in O(nlogn) time complexity.


class Solution:
    '''
     * @param nums an integer array
     * @param target an integer
     * @return the difference between the sum and the target
    '''
    def twoSumClosest(self, nums, target):

        nums.sort()
        l,r = 0 ,len(nums)-1

        diff = float('inf')

        while l<r:
            diff = min(diff, abs(nums[l] + nums[r] - target))

            if nums[l] + nums[r] > target:
                r-=1
            else:
                l+=1

        return diff

