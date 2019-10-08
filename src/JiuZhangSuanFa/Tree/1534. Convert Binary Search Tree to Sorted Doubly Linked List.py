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

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        # Write your code here.

        # pre = node.left
        # next = node.right

        if not root: return None

        def dfs(node):

            if not node: return None, None

            left_front, left_end = dfs(node.left)
            right_front, right_end = dfs(node.right)
            # pre
            node.left = left_end

            if left_end:
                left_end.right = node

            # next
            node.right = right_front

            if right_front:
                right_front.left = node

            if not left_front:
                left_front = node

            if not right_end:
                right_end = node

            return left_front, right_end

        left, right = dfs(root)
        left.left = right
        right.right = left
        return left


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(5)

print(Solution().treeToDoublyList(root))