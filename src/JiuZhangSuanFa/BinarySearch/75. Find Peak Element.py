# https://www.lintcode.com/problem/find-peak-element/description

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, nums):
        # write your code here
        if not nums: return -1

        l, r = 0, len(nums) - 1

        while l + 1 < r:

            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid

        return r if nums[r] > nums[l] else l