# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Same_Tree_100:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p is None and q is None:
            return True

        if p is None:
            return False

        if q is None:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Symmetric_Tree_101:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.symmetric(root.left, root.right)

    def symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return left.val == right.val and self.symmetric(left.left, right.right) and self.symmetric(left.right,
                                                                                                   right.left)

class Maximum_Depth_of_Binary_Tree_104:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1


class Balanced_Binary_Tree_110:

    def isBalanced(self, root: TreeNode) -> bool:

        if root is None:
            return True
        return self.maxDepth(root) >= 0

    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        if abs(r - l) > 1 or l < 0 or r < 0:
            return -10

        return max(l, r) + 1


class Minimum_Depth_of_Binary_Tree_111:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Subtree_of_Another_Tree_572:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSameTree(self, s:TreeNode, t:TreeNode) -> bool:

        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        return s.val == t.val and self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)


class Univalued_Binary_Tree_965:
    def isUnivalTree(self, root: TreeNode) -> bool:

        if root is None:
            return True

        if root.left is not None and root.left.val != root.val:
            return False

        if root.right is not None and root.right.val != root.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
