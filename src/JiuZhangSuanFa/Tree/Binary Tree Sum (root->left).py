#
# 给一棵二叉树，找出从根节点出发到叶节点的路径中，和最大的一条。
#
# 样例
#
# 给出如下的二叉树：
#
# 1
# / \
#     2   3
#
# 返回4。(最大的路径为1→3)
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def pathSum(self,root):

        if not root: return 0

        left = self.pathSum(root.left)
        right = self.pathSum(root.right)

        return root.val + max(left, right)




