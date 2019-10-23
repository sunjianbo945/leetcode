class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        left = 0

        for i in range(1, len(nums)):

            # not duplicates find
            if nums[i] != nums[left]:
                left += 1
                nums[i], nums[left] = nums[left], nums[i]

        return left + 1