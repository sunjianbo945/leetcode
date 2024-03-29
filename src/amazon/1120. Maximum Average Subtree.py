# Given the root of a binary tree, find the maximum average value of any subtree of that tree.
#
# (A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)
#
# leetcode question: https://leetcode.com/problems/maximum-average-subtree/

# Input: [5,6,1]
# Output: 6.00000
# Explanation:
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root) -> float:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            left_total, left_count = dfs(node.left)
            right_total, right_count = dfs(node.right)
            total = left_total + right_total + node.val
            count = right_count + left_count + 1
            res = max(res, total / count)
            return total, count

        dfs(root)
        return res
