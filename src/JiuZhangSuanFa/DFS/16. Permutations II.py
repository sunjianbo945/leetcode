class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        res = []
        self.recur(sorted(nums), [], res)

        return res

    def recur(self, nums, cur, res):

        if not nums:
            res.append(cur)
            return

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.recur(nums[:i] + nums[i + 1:], cur + [nums[i]], res)