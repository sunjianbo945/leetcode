# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Result:

    def __init__(self, val, local):
        self.path_val = val
        self.local = local


class Solution:
    def __init__(self):
        self.global_max = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0

        self.dfs(root)
        return self.global_max

    def dfs(self, node):

        if not node: return Result(0, 0)

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left_val = node.val + left.path_val
        right_val = node.val + right.path_val

        path_val = max(left_val, right_val, node.val)

        local_max = max(path_val, node.val + left.path_val + right.path_val)

        self.global_max = max(local_max, self.global_max)

        return Result(path_val, local_max)





