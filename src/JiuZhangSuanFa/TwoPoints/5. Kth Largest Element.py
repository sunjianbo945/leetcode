from typing import List


# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution215:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, l, r, n): # O(n) on average O(n^2) on worst case
        mid = self.partition(nums, l, r)

        if n == mid:
            return nums[mid]
        elif n > mid:
            return self.quickSelect(nums, mid + 1, r, n)
        else:
            return self.quickSelect(nums, l, mid - 1, n)

    def partition(self, nums, l, r):
        pviot = r
        target = nums[pviot]
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

        nums[l], nums[pviot] = nums[pviot], nums[l]
        return l

print(Solution().kthLargestElement(3,[9,3,2,4,8]))