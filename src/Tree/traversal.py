from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# 94. Binary Tree  Traversal
class Binary_Tree__Traversal_94:
    def Traversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.recur(root, ret)
        return ret

    def recur(self, root, ret):
        if root is None:
            return

        self.recur(root.left, ret)
        ret.append(root.val)
        self.recur(root.right, ret)


class N_ary_Tree_Preorder_Traversal_589:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        self.recur(root, ret)
        return ret

    def recur(self, node, ret):

        if node is None:
            return

        ret.append(node.val)
        for c in node.children:
            self.recur(c, ret)


class N_ary_Tree_Postorder_Traversal_590:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        self.recur(root, ret)
        return ret

    def recur(self, node, ret):
        if node is None:
            return
        for c in node.children:
            self.recur(c, ret)

        ret.append(node.val)
