
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Result:
    def __init__(self, height, is_balance):
        self.height = height
        self.is_balance = is_balance

    def __str__(self):
        return '{},{}'.format(self.height, self.is_balance)


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        return self.helper(root).is_balance

    def helper(self, node):

        if not node: return Result(0, True)

        left = self.helper(node.left)
        right = self.helper(node.right)
        print(left)
        print(right)
        if left.is_balance == False or right.is_balance == False:
            return Result(0, False)

        if abs(left.height - right.height) > 1:
            return Result(0, False)

        height = max(left.height, right.height) + 1
        return Result(height, True)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().isBalanced(root))