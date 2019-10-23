class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if not nums: return []
        if k > len(nums): return []

        l, r = 0, k
        total = 0
        for i in range(k):
            total += nums[i]
        res = [total]

        while r < len(nums):
            res.append(res[-1] - nums[l] + nums[r])
            r += 1
            l += 1

        return res