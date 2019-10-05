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
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here

        if not root:return []

        if not root.left and not root.right:return [root.val]


        if not root.left:
            res = self.dfs_right(root.right)
            leaves = self.dfs_leaves(root.right)
            return [root.val] + leaves + res

        if not root.right:
            res = self.dfs_left(root.left)
            leaves = self.dfs_leaves(root.left)
            return [root.val]  + res + leaves

        left = self.dfs_left(root.left)
        right = self.dfs_right(root.right)
        leaves = self.dfs_leaves(root)

        return [root.val]+left+leaves+right



    def dfs_left(self,node):

        if not node:return []
        # leaf
        if not node.left and not node.right:return []

        if node.left:
            left = self.dfs_left(node.left)
        else:
            left = self.dfs_left(node.right)

        return [node.val]+left


    def dfs_right(self,node):

        if not node: return []

        # leaf
        if not node.left and not node.right:return []

        if node.right:
            right = self.dfs_right(node.right)
        else:
            right = self.dfs_right(node.left)


        return right+[node.val]


    def dfs_leaves(self,node):

        if not node:return []

        if not node.left and not node.right:return [node.val]

        left = self.dfs_leaves(node.left)
        right = self.dfs_leaves(node.right)

        return left+right



root =  TreeNode(4)
root.left = TreeNode(1)
root.left.left=TreeNode(2)
root.left.left.left=TreeNode(3)

print(Solution().boundaryOfBinaryTree(root))












