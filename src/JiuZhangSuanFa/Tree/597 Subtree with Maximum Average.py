#  [LintCode] 597 Subtree with Maximum Average 解题报告
# Description
# Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
#
# Notice
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum average.
#
#
# Example
# Given a binary tree:
#
#      1
#     /   \
#  -5     11
#  / \     /  \
# 1   2 4    -2
#
# return the node 11.

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left,self.right=None,None

class Result:
    def __init__(self,n,total):
        self.n = n
        self.total = total


class Solution:
    def __init__(self):
        self.sub_tree = None
        self.sub_tree_average = float('-inf')

    def find_substree(self, root):
        self.find_substree_result(root)
        return self.sub_tree

    def find_substree_result(self, node):

        if not node:return Result(0,0)

        left = self.find_substree_result(node.left)
        right = self.find_substree_result(node.right)


        new_size = left.n+right.n+1
        new_total = left.total+right.total+node.val
        new_average = new_total/new_size

        if new_average>self.sub_tree_average:
            self.sub_tree_average=new_average
            self.sub_tree=node

        return Result(new_size,new_total)


root = TreeNode(1)
root.left=TreeNode(-5)
root.right=TreeNode(11)
root.left.right=TreeNode(1)
root.left.right=TreeNode(2)
root.right.left=TreeNode(4)
root.right.right=TreeNode(-2)

print(Solution().find_substree(root).val)

