"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        res = []
        self.pathSum(root, [], 0, res, target)
        return res

    def pathSum(self, node, cur_path, cur_sum, res, target):

        if not node:
            return

        if not node.left and not node.right and +node.val + cur_sum == target:
            res.append(cur_path + [node.val])
            return

        self.pathSum(node.left, cur_path + [node.val], cur_sum + node.val, res, target)
        self.pathSum(node.right, cur_path + [node.val], cur_sum + node.val, res, target)

