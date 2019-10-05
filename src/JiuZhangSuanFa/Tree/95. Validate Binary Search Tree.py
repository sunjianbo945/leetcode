"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Request:

    def __init__(self, min, max):
        self.min = min
        self.max = max


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        return self.helper(root, Request(float('-inf'), float('inf')))

    def helper(self, node, request):

        if not node: return True

        if node.val <= request.min or node.val >= request.max:
            return False

        if not self.helper(node.left, Request(request.min, node.val)) or not self.helper(node.right, Request(node.val,
                                                                                                             request.max)):
            return False

        return True
