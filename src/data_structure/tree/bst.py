import math
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# the beautiful property for BST is inorder traversal are sorted

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
class Solution1008:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def dfs(nodes, lb, rb):

            if not nodes: return None

            if lb < nodes[0] < rb:  # this is good
                val = nodes.pop(0)
                root = TreeNode(val)
                root.left = dfs(nodes, lb, val)
                root.right = dfs(nodes, val, rb)

                return root

            return None

        return dfs(preorder, float('-inf'), float('inf'))


# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
class Solution783:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node):
            if node:
                dfs(node.left)  # inorder traversal left

                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val

                dfs(node.right)  # inorder traversal right

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans


# https://leetcode.com/problems/recover-binary-search-tree/
class Solution99:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node: return

            inorder(node.left)  # inorder traversal left

            if node.val < self.pre.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder(node.right)  # inorder traversal right

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


# https://leetcode.com/problems/convert-bst-to-greater-tree/
class Solution538:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # right -> root -> left
        preSum = 0

        def dfs(node):
            nonlocal preSum
            if not node: return

            dfs(node.right)

            node.val = node.val + preSum
            preSum = node.val

            dfs(node.left)

        dfs(root)
        return root


# https://leetcode.com/problems/increasing-order-search-tree/
class Solution897:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal curr
            if not node: return

            dfs(node.left)

            node.left = None
            curr.right = node
            curr = node

            dfs(node.right)

        dummy = curr = TreeNode(None)
        dfs(root)
        return dummy.right


# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, lst):
            if not root: return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)

        lst1, lst2 = [], []
        inorder(root1, lst1)  # O(m)
        inorder(root2, lst2)  # O(n)

        i1, i2, res = 0, 0, []
        s1, s2 = len(lst1), len(lst2)

        while i1 < s1 and i2 < s2:  # merge two sorted array O(m+n)
            if lst1[i1] < lst2[i2]:
                res.append(lst1[i1])
                i1 += 1
            else:
                res.append(lst2[i2])
                i2 += 1

        return res + lst1[i1:] + lst2[i2:]

    def getAllElements_iterative(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []

        while root1 or root2 or stack1 or stack2:
            # update both stacks
            # by going left till possible
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right

        return output


# https://leetcode.com/problems/validate-binary-search-tree/
class Solution98:
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(node, lb, rb):

            if not node: return True

            if lb < node.val < rb:
                return dfs(node.left, lb, node.val) and dfs(node.right, node.val, rb)

            return False

        return dfs(root, float('-inf'), float('inf'))


# https://leetcode.com/problems/largest-bst-subtree/
class Solution333:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node: return True, 0, math.inf, -math.inf

            isl, lCount, lMin, lMax = dfs(node.left)
            isr, rCount, rMin, rMax = dfs(node.right)

            if isl and isr and lMax < node.val < rMin:
                count = max(count, lCount + rCount + 1)
                return True, lCount + rCount + 1, min(lMin, node.val), max(rMax, node.val)
            else:
                return False, 0, 0, 0

        dfs(root)
        return count


# https://leetcode.com/problems/binary-search-tree-iterator/
# https://leetcode.com/problems/binary-search-tree-iterator-ii/solution/
class BSTIterator173:
    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, root):
        if not root: return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)
    # def __init__(self, root: TreeNode):
    #     self.stack = []
    #     while root:
    #         self.stack.append(root)
    #         root = root.left
    #
    # def next(self) -> int:
    #     curr = self.stack.pop()
    #     temp = curr
    #     if temp.right:
    #         temp = temp.right
    #         while temp:
    #             self.stack.append(temp)
    #             temp = temp.left
    #
    #     return curr.val
    #
    # def hasNext(self) -> bool:
    #     return self.stack
