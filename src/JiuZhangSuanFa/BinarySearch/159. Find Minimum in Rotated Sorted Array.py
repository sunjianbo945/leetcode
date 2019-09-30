# https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        if not nums: return -1

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        benchmark = nums[0]

        while l + 1 < r:

            mid = (l + r) // 2

            if nums[mid] < benchmark:
                r = mid
            else:
                l = mid

        return nums[r] if nums[r] < nums[l] else nums[l]
