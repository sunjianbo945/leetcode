"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # write your code here

        if not root: return []

        queue = [root]

        res = []

        forward = True

        while queue:

            size = len(queue)

            level = []

            for i in range(size):
                node = queue.pop(0)
                if forward:
                    level.append(node.val)
                else:
                    level = [node.val] + level

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(level)
            forward = (not forward)

        return res
