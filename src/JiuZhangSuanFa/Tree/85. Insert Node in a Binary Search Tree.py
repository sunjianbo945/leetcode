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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if not root: return node

        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:

            root.right = self.insertNode(root.right, node)

        return root


    def insertNodeIterative(self, root, node):
        # write your code here
        if not root: return node

        temp = root

        while temp:

            if temp.val < node.val:

                if temp.right is None:
                    temp.right = node
                    return root
                else:
                    temp = temp.right

            else:

                if temp.left is None:
                    temp.left = node
                    return root
                else:
                    temp = temp.left

        return root