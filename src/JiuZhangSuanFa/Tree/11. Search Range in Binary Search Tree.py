"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here

        if not root: return []

        left = self.searchRange(root.left, k1, k2)
        right = self.searchRange(root.right, k1, k2)

        res = []
        if root.val >= k1 and root.val <= k2:
            res = [root.val]

        res = left + res + right

        return res
