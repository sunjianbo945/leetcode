# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.
#
# Example 1:
#
# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47
#
# Example 2:
#
# Input: nums = [1, 1], target = 2
# Output: 1
# Explanation:
# 1 + 1 = 2
#
# Example 3:
#
# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.


def find(nums,target):

    nums = sorted(nums)

    l, r = 0,len(nums)-1

    total =0

    while l<r:

        if nums[l]+nums[r] == target:

            total+=1
            l+=1
            r-=1

            while l<r and nums[l-1] == nums[l]:
                l+=1

            while l<r and nums[r]==nums[r+1]:
                r-=1
        elif nums[l]+nums[r]<target:
            l+=1
        else:
            r-=1

    return total

print(find([1, 1, 2, 45, 46, 46],47))

print(find([1, 1],2))


print(find([1,5, 1,5],6))
