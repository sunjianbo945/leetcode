class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []

        queue = [0]

        for i in range(1, k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

        res = [nums[queue[0]]]

        for i in range(k, len(nums)):

            while queue and i - k >= queue[0]:
                queue.pop(0)

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            res.append(nums[queue[0]])

        return res