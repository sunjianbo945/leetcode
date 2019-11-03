# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res = []

        while queue:

            node = queue.pop(0)

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        root_val = vals.pop(0)
        if root_val == '#': return None
        root = TreeNode(root_val)

        queue = [root]

        while queue and vals:

            node = queue.pop(0)

            left_val = vals.pop(0)
            right_val = vals.pop(0)

            left = TreeNode(left_val) if left_val != '#' else None
            right = TreeNode(right_val) if right_val != '#' else None

            node.left = left
            node.right = right

            if left: queue.append(left)
            if right: queue.append(right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))