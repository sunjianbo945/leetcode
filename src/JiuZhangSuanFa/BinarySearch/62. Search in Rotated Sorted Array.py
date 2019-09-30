# https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, nums, target):
        # write your code here
        if not nums: return -1

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            # print('{} {}'.format(l,r))
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target >= nums[l]:

                if target > nums[mid] and nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid
            else:

                if target < nums[mid] and nums[mid] < nums[l]:
                    r = mid
                else:
                    l = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        return -1