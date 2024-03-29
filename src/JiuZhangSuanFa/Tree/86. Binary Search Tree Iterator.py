"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        # write your code here
        return self.stack

    """
    @return: return next node
    """

    def next(self, ):
        # write your code here
        node = self.stack.pop()
        cur = node
        if cur.right:
            self.stack.append(cur.right)
            cur = cur.right

            while cur.left:
                self.stack.append(cur.left)
                cur = cur.left

        return node

