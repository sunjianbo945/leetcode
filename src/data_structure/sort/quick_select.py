# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution215:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here

        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - n)

    def quickSelect(self, nums, left, right, n):

        mid = self.partition(nums, left, right)

        if n == mid:
            return nums[mid]
        elif n > mid:
            return self.quickSelect(nums, mid + 1, right, n)
        else:
            return self.quickSelect(nums, left, mid - 1, n)

    def partition(self, nums, l, r):

        target = nums[r]
        r -= 1

        while l <= r:  # finally l is on the right of r
            while l <= r and nums[l] < target:
                l += 1

            while l <= r and nums[r] >= target:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        nums[l], nums[r] = nums[r], nums[l]
        return l


print(Solution().kthLargestElement(3, [9, 3, 2, 4, 8]))
