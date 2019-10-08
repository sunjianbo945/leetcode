"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        # write your code here
        if not root: return None

        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:

            if not root.right:
                return root.left

            if not root.left:
                return root.right

            temp = root.right

            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.removeNode(root.right, temp.val)

        return root
