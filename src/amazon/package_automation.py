# Amazon's Fulfillment Center consists of a packaging bay where orders are automatically packaged in groups(n). The first group can only have 1 item and all the subsequent groups can have one item more than the previous group. Given a list of items on groups, perform certain operations in order to satisfy the constraints required by packaging automation.
# The conditions are as follows:
#
# The first group must contain 1 item only.
# For all other groups, the difference between the number of items in adjacent groups must not be greater than 1. In other words, for 1<=i<n, arr[i]-arr[i-1]<=1
# To accomplish this, the following operations are available.
#
# Rearrange the groups in any way.
# Reduce any group to any number that is at least 1
# Write an algorithm to find the maximum number of items that can be packaged in the last group with the conditions in place.
#
# Input
# The function/method consists of two arguments:
# numGroups, an integer representing the number of groups(n);
# arr, a list of integers representing the number of items in each group
#
# Output
# Return an integer representing the maximum items that can be packaged for the final group of the list given the conditions above.

#
# 第一遍count frequency
# 第二遍从 1到len(arr)+1(用while), 检查dictionary里有没有这个数字，有的话就都堆上res array, 没有的话就只能放比上一个数大1的数（从以后更大的数字借的，要记住借了多少个），
# 直到下一个有的数存在时，堆上的时候要减去以前借了多少个
from collections import Counter
class Solution:
    def sort(self, arr):
        num_count = Counter(arr)

