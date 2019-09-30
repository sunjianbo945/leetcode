# https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        if not nums: return 0

        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums) - 1

        while l + 1 < r:

            mid = l + (r - l) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid

        if nums[l] > nums[l + 1]:
            return nums[l]
        else:
            return nums[r]

