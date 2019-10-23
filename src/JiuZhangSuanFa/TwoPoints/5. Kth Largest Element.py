class Solution:
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

    def partition(self, nums, left, right):

        target = nums[right]
        end = right - 1
        start = left

        while start <= end:

            while start <= end and nums[start] < target:
                start += 1

            while start <= end and nums[end] >= target:
                end -= 1

            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        nums[start], nums[right] = nums[right], nums[start]
        return start

print(Solution().kthLargestElement(3,[9,3,2,4,8]))