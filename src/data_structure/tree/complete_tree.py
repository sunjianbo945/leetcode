from typing import List

from src.data_structure.tree.model import TreeNode


# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
class Solution1104:
    def pathInZigZagTree(self, label: int) -> List[int]: # O(d)
        level, tot = -1, 0
        while label > tot:
            level += 1
            tot += (2 ** level)

        level -= 1
        cur = label // 2
        res = [label]
        while level > -1:
            st, end = 2 ** level, (2 ** (level + 1)) - 1
            cur = st + end - cur  # the reason this work since two node from most left + most right are switched
            res.append(cur)
            level -= 1
            cur = cur // 2
        return res[::-1]


# https://leetcode.com/problems/count-complete-tree-nodes/
class Solution222:
    def countNodes(self, root: TreeNode) -> int:  # O (logn*logn)
        ## RC ##
        ## APPROACH : RECURSION ##
        ## TIME COMPLEXICITY : LOG N * LOG N ##

        ## LOGIC ##
        # If left sub tree height equals right sub tree height then,
        #       a. left sub tree is perfect binary tree
        #       b. right sub tree is complete binary tree
        # If left sub tree height greater than right sub tree height then,
        #       a. left sub tree is complete binary tree
        #       b. right sub tree is perfect binary tree

        if not root:
            return 0

        def depthLeft(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def depthRight(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        ld = depthLeft(root.left)
        rd = depthRight(root.right)

        if ld == rd:
            return 2 ** (ld + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
