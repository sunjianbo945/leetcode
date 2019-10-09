"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        # write your code here
        if not root: return []

        res = []

        queue = [root]

        while queue:

            size = len(queue)
            level = []

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res = [level] + res

        return res
