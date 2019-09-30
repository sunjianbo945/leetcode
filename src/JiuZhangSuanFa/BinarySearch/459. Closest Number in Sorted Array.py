#[LintCode] Closest Number in Sorted Array
#
# Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.
#
# Return -1 if there is no element in the array.
#  Notice
#
# There can be duplicate elements in the array, and we can return any of the indices with same value.

# Example
#
# Given [1, 2, 3] and target = 2, return 1.
#
# Given [1, 4, 6] and target = 3, return 1.
#
# Given [1, 4, 6] and target = 5, return 1 or 2.
#
# Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.
# Challenge
#
# O(logn) time complexity.

class Solution:

    def find_closest_num(self, nums, target):
        if not nums:return -1
        l,r = 0,len(nums)-1

        while l+1<r:

            mid = (l+r)//2

            if nums[mid] == target:
                r=mid
            elif nums[mid]<target:
                l=mid
            else:
                r=mid

        left_diff = abs(nums[l]-target)
        right_diff = abs(nums[r]-target)

        if left_diff<right_diff:
            return l
        else:
            return r


if __name__ == '__main__':
    print(Solution().find_closest_num([1, 2, 3],2))
    print(Solution().find_closest_num([1, 4, 6],3))
    print(Solution().find_closest_num([1, 4, 6],5))
    print(Solution().find_closest_num([1, 3, 3, 4],2))