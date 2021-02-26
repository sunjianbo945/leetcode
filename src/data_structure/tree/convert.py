from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class Solution108:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(l, r):  # r not include

            if l >= r: return None

            mid = (l + r) // 2

            root = TreeNode(nums[mid])
            root.left = dfs(l, mid)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(nums))


# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
class Solution109:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def get(head):
            vals = []
            while head:
                vals.append(head.val)
                head = head.next
            return vals

        values = get(head)

        def dfs(l, r):
            if l >= r: return None

            mid = (l + r) // 2
            node = TreeNode(values[mid])

            # Recursively form BST on the two halves
            node.left = dfs(l, mid)
            node.right = dfs(mid + 1, r)
            return node

        return dfs(0, len(values))

    def sortedListToBST_nlogn(self, head: ListNode) -> TreeNode:
        if not head: return None

        def getMid(node):
            if not node: return None
            if not node.next: return node
            prev = None
            slow, fast = node, node

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev: prev.next = None
            return slow

        mid = getMid(head)

        root = TreeNode(mid.val)
        if head == mid: return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root


# https://leetcode.com/problems/balance-a-binary-search-tree/
class Solution1382:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            """inorder depth-first traverse bst"""
            if not node: return
            dfs(node.left)
            value.append(node.val)
            dfs(node.right)

        value = []  # collect values
        dfs(root)

        def tree(lo, hi):
            if lo > hi: return None
            mid = (lo + hi) // 2
            ans = TreeNode(value[mid])
            ans.left = tree(lo, mid - 1)
            ans.right = tree(mid + 1, hi)
            return ans

        return tree(0, len(value) - 1)

    # def rotateLeft(x: TreeNode, p: TreeNode) -> TreeNode:
    #     y = x.right
    #     x.right = y.left
    #     y.left = x
    #
    #     if p.left == x:
    #         p.left = y
    #     else:
    #         p.right = y
    #
    #     return y
    #
    # def rotateRight(x: TreeNode, p: TreeNode) -> TreeNode:
    #     y = x.left
    #     x.left = y.right
    #     y.right = x
    #
    #     if p.left == x:
    #         p.left = y
    #     else:
    #         p.right = y
    #
    #     return y
    #
    # def getHeight(node: TreeNode) -> int:
    #     if not node:
    #         return 0
    #
    #     return max(getHeight(node.left), getHeight(node.right)) + 1
    #
    # def recBalance(node: TreeNode, p: TreeNode) -> tuple:
    #     if not node:
    #         return 0, 0
    #
    #     left_height, left_balance = recBalance(node.left, node)
    #     right_height, right_balance = recBalance(node.right, node)
    #
    #     node_balance = left_height - right_height
    #
    #     if node_balance > 1:
    #         if left_balance < 0:
    #             rotateLeft(node.left, node)
    #         return recBalance(rotateRight(node, p), p)
    #     elif node_balance < -1:
    #         if right_balance > 0:
    #             rotateRight(node.right, node)
    #         return recBalance(rotateLeft(node, p), p)
    #     else:
    #         left_height, right_height = getHeight(node.left), getHeight(node.right)
    #         return max(left_height, right_height) + 1, left_height - right_height
    #
    # dummy = TreeNode(None)
    # dummy.right = root
    # recBalance(dummy.right, dummy)
    # return dummy.right


# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
class Solution114:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node: return None
            if not node.left and not node.right: return node  # return the leaf node

            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if leftTail:  # leftTail can be None when no left child
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail if rightTail else leftTail  # rightTail can be None when no right chile

        dfs(root)

    def flatten_iterative(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        curr = root
        while curr:
            # If the node has a left child
            if curr.left:
                # Find the rightmost node
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = curr.right
                curr.right = curr.left
                curr.left = None

            # move on to the right side of the tree
            curr = curr.right


# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
class Solution426:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root

        def dfs(node):
            if not node: return None, None

            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            if lr:
                node.left = lr
                lr.right = node

            if rl:
                node.right = rl
                rl.left = node

            ll = ll if ll else node
            rr = rr if rr else node
            return ll, rr

        l, r = dfs(root)
        l.left = r
        r.right = l
        return l
