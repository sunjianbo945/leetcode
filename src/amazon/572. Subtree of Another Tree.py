# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if not s and not t:
            return True

        if not s or not t:
            return False

        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):

        if not t and not s:
            return True

        if not t or not s:
            return False

        if s.val != t.val:
            return False

        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)