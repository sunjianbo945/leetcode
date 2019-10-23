#  [LintCode] 587 Two Sum - Unique pairs 解题报告
# Description
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
#
#
#
# Example
# Given nums = [1,1,2,45,46,46], target = 47
# return 2
#
# 1 + 46 = 47
# 2 + 45 = 47

class Solution:
    '''
     * @param nums an array of integer
     * @param target an integer
     * @return an integer
     '''
    def twoSum6(self, nums,  target):

        nums.sort()

        l,r = 0,len(nums)-1
        count = 0
        while l<r:

            if nums[l]+nums[r]< target:
                l+=1
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                count +=1
                l+=1
                r-=1

                while l<r and nums[l]==nums[l-1]:
                    l+=1

                while l<r and nums[r] == nums[r+1]:
                    r-=1

        return count
