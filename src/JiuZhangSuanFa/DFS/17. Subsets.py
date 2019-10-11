class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        res = []

        self.dfs(sorted(nums), 0, [], res)

        return res

    def dfs(self, nums, index, cur, res):

        res.append(cur)

        if index >= len(nums):
            return

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, cur + [nums[i]], res)
