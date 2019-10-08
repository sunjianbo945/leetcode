"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Result:

    def __init__(self, node, A, B):
        self.node = node
        self.A = A
        self.B = B


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        res = self.dfs(root, A, B)
        if res.A and res.B:
            return res.node

        return None

    def dfs(self, node, A, B):
        if not node: return Result(None, False, False)

        left = self.dfs(node.left, A, B)
        right = self.dfs(node.right, A, B)

        a_exist = left.A or right.A or node.val == A.val
        b_exist = left.B or right.B or node.val == B.val

        if A.val == node.val or B.val == node.val:
            return Result(node, a_exist, b_exist)

        if left.node and right.node:
            return Result(node, a_exist, b_exist)

        if left.node:
            return Result(left.node, a_exist, b_exist)

        if right.node:
            return Result(right.node, a_exist, b_exist)

        return Result(None, a_exist, b_exist)

root=TreeNode(4)
root.left=TreeNode(3)
root.right=TreeNode(7)
root.right.left=TreeNode(5)
root.right.right=TreeNode(6)

print(Solution().lowestCommonAncestor3(root,TreeNode(5),TreeNode(6)))