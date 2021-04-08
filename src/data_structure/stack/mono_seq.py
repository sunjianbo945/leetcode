from collections import defaultdict
from math import inf
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

# https://www.includehelp.com/algorithms/find-nearest-greatest-neighbours-of-each-element-in-an-array.aspx







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


# https://leetcode.com/problems/maximal-rectangle/
class Solution85:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n = len(matrix[0])
        if n == 0: return 0

        def hist(arr):
            arr = arr + [0]
            stack = [-1]
            res = 0
            for i in range(len(arr)):
                while len(stack) > 1 and arr[stack[-1]] > arr[i]:
                    pos = stack.pop()
                    res = max(res, (i - stack[-1] - 1) * arr[pos])

                stack.append(i)

            return res

        res = 0
        h = [0] * n
        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0

            res = max(res, hist(h))

        return res

# https://leetcode.com/problems/remove-k-digits/
class Solution402:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []  # increase sequence

        for num in nums:
            while k and stack and stack[-1] > num:
                stack.pop()
                k -= 1

            stack.append(num)

        stack = stack[:-k] if k else stack

        return "".join(stack).lstrip('0') or "0"


# https://leetcode.com/problems/daily-temperatures/
class Solution739:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        n = len(T)
        res = [0] * n

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:  # decreasing stack
                last_idx = stack.pop()
                res[last_idx] = i - last_idx

            stack.append(i)

        return res


# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
class Solution1130:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [inf]
        res = 0
        for i, num in enumerate(arr):
            while stack and stack[-1] < num:  # decreasing
                local_min = stack.pop()
                res += min(num, stack[-1]) * local_min

            stack.append(num)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res