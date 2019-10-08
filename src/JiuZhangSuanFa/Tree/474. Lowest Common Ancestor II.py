"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # write your code here

        A_map = {}

        temp = A
        while temp is not None:
            A_map[temp.val] = temp
            temp = temp.parent

        temp = B
        while temp is not None:

            if temp.val in A_map:
                return A_map[temp.val]

            temp = temp.parent

        return None