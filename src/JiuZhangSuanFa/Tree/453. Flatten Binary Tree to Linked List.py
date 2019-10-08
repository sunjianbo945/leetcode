"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:return
        def dfs(node):

            if not node:return None, None

            left_start,left_end = dfs(node.left)
            right_start,right_end = dfs(node.right)

            # root.right ->  left front
            if left_start:
                node.right = left_start
            #root.left -> None
            node.left = None

            # left end goes to right front
            if left_end:
                left_end.right = right_start

            # right end is empty, then consider left end or roor
            if not right_end:
                if left_end:
                    right_end=left_end
                else:
                    right_end = node

            return node,right_end

        dfs(root)


