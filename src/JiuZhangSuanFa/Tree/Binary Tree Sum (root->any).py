# 2.4 Binary Tree Maximum Path Sum II
#
# http://www.lintcode.com/zh-cn/problem/binary-tree-maximum-path-sum-ii/
#
#     给一棵二叉树，找出从根节点出发的路径中，和最大的一条。
#
#     这条路径可以在任何二叉树中的节点结束，但是必须包含至少一个点（也就是根了）。
#
#     样例
#
#     给出如下的二叉树：
#
#       1
#      / \
#     2   3
#
#     返回4。(最大的路径为1→3)
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def pathSum(self,root):

        if not root: return 0

        left = self.pathSum(root.left)
        right = self.pathSum(root.right)

        return root.val + max(left, right, 0)
