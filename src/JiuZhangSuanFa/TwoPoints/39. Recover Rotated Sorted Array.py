class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here

        index = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                index = i - 1
                break
        if index == -1:
            return

        self.reverse(nums, 0, index)
        self.reverse(nums, index + 1, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):

        if start >= end: return

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1