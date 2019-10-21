class Pair:
    def __init__(self, index, sum_num):
        self.index = index
        self.sum_num = sum_num


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        pre_sum = [Pair(0, 0)]
        sum_num = 0
        for i in range(len(nums)):
            sum_num += nums[i]
            pre_sum.append(Pair(i + 1, sum_num))

        pre_sum_soreted = sorted(pre_sum, key=lambda x: x.sum_num)

        closet = float('inf')
        res = []

        for i in range(1, len(pre_sum_soreted)):

            if pre_sum_soreted[i].sum_num - pre_sum_soreted[i - 1].sum_num < closet:
                closet = pre_sum_soreted[i].sum_num - pre_sum_soreted[i - 1].sum_num
                left = min(pre_sum_soreted[i].index, pre_sum_soreted[i - 1].index)
                right = max(pre_sum_soreted[i].index, pre_sum_soreted[i - 1].index) - 1
                res = [left, right]

        return res