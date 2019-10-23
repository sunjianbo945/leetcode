class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here

        S.sort()
        total = 0
        for i in range(len(S) - 1, 1, -1):
            total += self.test(S, i - 1, S[i])

        return total

    def test(self, nums, end, target):
        if end <= 0:
            return 0

        total = 0
        start = 0

        while start < end:
            if nums[start] + nums[end] <= target:
                start += 1
            else:
                total += (end - start)
                end -= 1
                # while start< end and nums[end] == nums[end+1]:
                #     end-=1

        return total