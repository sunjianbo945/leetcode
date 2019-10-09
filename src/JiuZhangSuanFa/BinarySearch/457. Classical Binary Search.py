class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here

        if not nums: return -1
        l, r = 0, len(nums) - 1

        while l + 1 < r:

            mid = l + (r - l) // 2

            if nums[mid] <= target:
                l = mid
            else:
                r = mid

        if nums[l] == target:
            return l

        if nums[r] == target:
            return r

        return -1