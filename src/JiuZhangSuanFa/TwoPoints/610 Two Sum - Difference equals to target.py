#  [LintCode] 610 Two Sum - Difference equals to target 解题报告
# Description
# Given an array of integers, find two numbers that their difference equals to a target value.
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
#
#
# Notice
# It's guaranteed there is only one available solution
#
#
#
# Example
# Given nums = [2, 7, 15, 24], target = 5
# return [1, 2] (7 - 2 = 5)

class Pair:
    def __init__(self, index, num):
        self.index = index
        self.num = num

class Solution:

    def find(self, nums, target):

        pairs = [ Pair(i,nums[i]) for i in range(len(nums))]

        pairs.sort(key=lambda x :x.num)

        j=0
        for i in range(1,len(pairs)):

            while j<i and j<len(pairs) and pairs[i].num-pairs[j].num > target:
                j+=1

            if pairs[i].num-pairs[j].num == target:
                l = pairs[i].index if pairs[i].index < pairs[j].index else pairs[j].index
                r =  pairs[i].index if pairs[i].index > pairs[j].index else pairs[j].index
                return [l+1,r+1]


        return []













