"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BFSSolution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if not root: return ''
        res = []
        queue = [root]
        while queue:

            node = queue.pop(0)
            if node is None:
                res.append('#')
            else:
                res.append(str(node.val))

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(res)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here

        if not data: return None

        nodes = data.split(',')
        if not nodes: return None

        root = TreeNode(int(nodes.pop(0)))
        queue = [root]
        while queue and nodes:

            top = queue.pop(0)
            top.left = self._createNode(data)
            top.right = self._createNode(data)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)

        return root

    def _createNode(self, data_collection):
        if not data_collection: return None
        data = data_collection.pop(0)

        if data == '#': return None
        return TreeNode(int(data))


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class DFSSolution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if not root: return 'x'
        return '{},{},{}'.format(root.val, self.serialize(root.left), self.serialize(root.right))

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here

        array = data.split(',')

        def dfs(data):
            if not data: return None

            val = data.pop(0)

            if val == 'x': return None

            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        return dfs(array)
