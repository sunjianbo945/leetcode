from collections import defaultdict
from typing import List


# https://leetcode.com/problems/next-greater-element-i/
class Solution496:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = defaultdict(int)
        next_greater.default_factory = lambda: -1

        for num in nums2:
            while stack and stack[-1] < num:  # non-increasing
                next_greater[stack.pop()] = num

            stack.append(num)

        return [next_greater[num] for num in nums1]


# https://leetcode.com/problems/next-greater-element-ii/
class Solution503:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:  # non-increasing
                pos = stack.pop()
                res[pos] = nums[i]

            stack.append(i)

        return res[:n // 2]


# https://leetcode.com/problems/online-stock-span/
class StockSpanner901:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution84:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stack = [-1]
        res = 0
        for idx, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                pos = stack.pop()
                height = heights[pos]
                width = idx - stack[-1] - 1
                res = max(res, height * width)

            stack.append(idx)

        return res