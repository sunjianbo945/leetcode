# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Validate_Binary_Search_Tree_98:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node: TreeNode, lower, upper) -> bool:

        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        return self.helper(node.left, lower, node.val) and self.helper(node.right, node.val, upper)


class Minimum_Absolute_Difference_in_BST_530:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node: TreeNode, lower, upper):
        if not node:
            return upper - lower

        left = self.helper(node.left, lower, node.val)
        right = self.helper(node.right, node.val, upper)
        return min(left, right)
