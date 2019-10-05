"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if not root: return []

        if not root.left and not root.right:
            return ['{}'.format(root.val)]

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        res = []
        if left:
            for path in left:
                res.append('{}->{}'.format(root.val, path))

        if right:
            for path in right:
                res.append('{}->{}'.format(root.val, path))

        return res


