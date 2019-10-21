class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        sum_num = 0
        max_num = float('-inf')
        min_num = 0
        for num in nums:
            sum_num+=num
            max_num = max(max_num,sum_num-min_num)
            min_num = min(sum_num,min_num)


        return max_num