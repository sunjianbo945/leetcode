# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Diameter_of_Binary_Tree_543(object):
    def diameterOfBinaryTree(self, root):
        self.glob_max = 1

        def helper(node):
            if not node: return 0
            L = helper(node.left)
            R = helper(node.right)
            self.glob_max = max(self.glob_max, L + R + 1)
            return max(L, R) + 1

        helper(root)
        return self.glob_max - 1


class Binary_Tree_Maximum_Path_Sum_124:
    def maxPathSum(self, root: TreeNode) -> int:
        self.glob_max = float('-inf')
        def helper(node):
            if not node: return 0
            l = max(helper(node.left), 0)
            r = max(helper(node.right), 0)
            self.glob_max = max(self.glob_max, node.val + l + r)
            return node.val + max(l, r)

        helper(root)
        return self.glob_max



class Longest_Univalue_Path_687:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.glob_max = 1
        def helper(node):
            if not node: return 0
            lp,rp=0,0
            l = helper(node.left)
            if node.left is not None and node.left.val==node.val:
                lp=l
            r = helper(node.right)
            if node.right is not None and node.right.val==node.val:
                rp=r
            self.glob_max = max(self.glob_max, 1 + lp + rp)
            return 1 + max(lp, rp)

        helper(root)
        return self.glob_max-1


