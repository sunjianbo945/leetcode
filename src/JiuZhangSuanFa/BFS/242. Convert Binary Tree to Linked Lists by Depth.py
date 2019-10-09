"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here

        if not root: return []

        queue = [root]

        res = []

        while queue:

            size = len(queue)

            dummy = ListNode(0)
            cur = dummy
            for i in range(size):

                node = queue.pop(0)

                cur.next = ListNode(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                cur = cur.next

            res.append(dummy.next)

        return res