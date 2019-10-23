class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        first_zero_p = 0

        loop_p = 0

        while loop_p < len(nums):

            if nums[loop_p] != 0:

                # nums[loop_p] != 0 then need to swap with first_zero_p place
                while first_zero_p < loop_p and nums[first_zero_p] != 0:
                    first_zero_p += 1

                nums[first_zero_p], nums[loop_p] = nums[loop_p], nums[first_zero_p]

            loop_p += 1