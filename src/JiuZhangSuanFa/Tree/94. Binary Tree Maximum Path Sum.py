class Result:
    def __init__(self):
        self.path_max = float('-inf')
        self.global_max = float('-inf')


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        if not root: return 0
        return self.helper(root).global_max

    def helper(self, root):
        if not root: return Result()

        left = self.helper(root.left)
        right = self.helper(root.right)

        res = Result()
        res.path_max = max(root.val, root.val + left.path_max, root.val + right.path_max)
        res.global_max = max(left.global_max, right.global_max, res.path_max, root.val + left.path_max + right.path_max)

        return res