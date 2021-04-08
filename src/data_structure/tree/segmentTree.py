from typing import List


#
# https://leetcode.com/problems/range-sum-query-mutable/
class NumArray307:

    def __init__(self, nums: List[int]):
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, arr, start, end):
        if start == end:
            return SegmentTreeNode(start, end, arr[start])

        mid = (start + end) // 2
        left = self.buildTree(arr, start, mid)
        right = self.buildTree(arr, mid + 1, end)
        return SegmentTreeNode(start, end, left.total + right.total, left, right)

    def update(self, index: int, val: int) -> None:

        def dfs(node):
            if node.start == node.end == index:
                node.total = val
                return

            mid = (node.start + node.end) // 2

            if index <= mid:
                dfs(node.left)
            else:
                dfs(node.right)

            node.total = node.left.total + node.right.total

        dfs(self.root)

    def sumRange(self, left: int, right: int) -> int:

        def dfs(node, i, j):
            if node.start == i and node.end == j:
                return node.total

            mid = (node.start + node.end) // 2

            if i > mid:
                return dfs(node.right, i, j)
            elif j <= mid:
                return dfs(node.left, i, j)
            else:
                return dfs(node.left, i, mid) + dfs(node.right, mid + 1, j)

        return dfs(self.root, left, right)


class SegmentTreeNode:

    def __init__(self, start, end, total=0, left=None, right=None):
        self.start = start
        self.end = end
        self.total = total
        self.left = left
        self.right = right
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
