"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:

    def __init__(self):
        self.subtree_sum = float('inf')
        self.subtree = None

    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        self.findSubtreeSum(root)
        return self.subtree

    def findSubtreeSum(self, node):
        if not node: return 0

        left = self.findSubtreeSum(node.left)
        right = self.findSubtreeSum(node.right)

        sum = left + right + node.val

        if sum < self.subtree_sum:
            self.subtree_sum = sum
            self.subtree = node

        return sum