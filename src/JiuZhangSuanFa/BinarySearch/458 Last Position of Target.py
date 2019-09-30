# LintCode 458. Last Position of Target
#
# Find the last position of a target number in a sorted array. Return -1 if target does not exist.
#
# Example
#
# Given [1, 2, 2, 4, 5, 5].
#
# For target = 2, return 2.
#
# For target = 5, return 5.
#
# For target = 6, return -1.

class Solution:
    def lastPosition(self,nums,target):
        if not nums:return -1

        l,r = 0,len(nums)-1

        while l+1<r:
            mid = l +(r-l)//2
            if target >= nums[mid]:
                l=mid
            else:
                r=mid

        if nums[r]==target:
            return r

        if nums[l] == target:
            return l

        return -1

if __name__=='__main__':
    print(Solution().lastPosition([1, 2, 2, 4, 5, 5],2))
    print(Solution().lastPosition([1, 2, 2, 4, 5, 5],5))
    print(Solution().lastPosition([1, 2, 2, 4, 5, 5],6))