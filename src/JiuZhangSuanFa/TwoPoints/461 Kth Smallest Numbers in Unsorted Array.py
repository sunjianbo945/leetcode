#  [LintCode] 461 Kth Smallest Numbers in Unsorted Array 解题报告
# Description
# Find the kth smallest numbers in an unsorted integer array.
#
#
# Example
# Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].
#
#
# Challenge
# An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.

class Solution:
    '''
     * @param k an integer
     * @param nums an integer array
     * @return kth smallest element
    '''
    def kthSmallest(self, k, nums):
        return self.quickSelect(0,len(nums)-1, nums,k-1)


    def quickSelect(self, left,right, nums, k):
        mid = self.partition(left,right,nums)

        if mid == k:
            return nums[k]
        elif mid>k:
            return self.quickSelect(left,mid-1, nums,k)
        else:
            return self.quickSelect(mid+1,right,nums,k)


    def partition(self,start, end, nums):
        last = end
        target = nums[end]
        end = end-1

        while start<=end:

            while start<=end and nums[start] < target:
                start+=1

            while start<=end and nums[end] >= target:
                end-=1

            if start<=end:
                nums[start] , nums[end] = nums[end] , nums[start]
                start+=1
                end-=1

        nums[last], nums[start] = nums[start], nums[last]
        return start



nums = [3, 4, 1, 2, 5]
for i in range(len(nums)):
    # print(i)
    print(Solution().kthSmallest(i+1, nums))











