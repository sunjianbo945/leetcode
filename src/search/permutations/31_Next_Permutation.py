

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return

        def swap(nums, n1, n2):
            temp = nums[n1]
            nums[n1] = nums[n2]
            nums[n2] = temp

        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1

        i = len(nums) - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            swap(nums, i, j)
        reverse(nums, i + 1)



def main():
    print(Solution().nextPermutation([1,2,3]))


if __name__=='__main__':
    main()
