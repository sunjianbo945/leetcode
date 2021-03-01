from collections import *
from functools import lru_cache
from typing import *

from src.data_structure.tree.model import TreeNode, Node


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


# https://leetcode.com/problems/serialize-and-deserialize-bst/submissions/
class Codec449:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))


# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class Codec297:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # preorder traversal
        def dfs(node):
            if not node: return '#'
            return '{},{},{}'.format(node.val, dfs(node.left), dfs(node.right))

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split(',')

        def dfs(nodes):
            if not nodes: return None
            val = nodes.pop(0)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node

        return dfs(nodes)

    def serialize_bfs(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # preorder traversal
        if not root: return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')

        return ','.join(map(str, res))

    def deserialize_bfs(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes.pop(0)))
        queue = [root]

        while queue:
            curr = queue.pop(0)
            left_val = nodes.pop(0)
            right_val = nodes.pop(0)
            curr.left = TreeNode(int(left_val)) if left_val != '#' else None
            curr.right = TreeNode(int(right_val)) if right_val != '#' else None
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)

        return root


# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
class Codec428:
    def serialize(self, root: 'Node') -> str:
        def encode(node: 'Node'):
            if not node: return '$'
            yield f'{node.val}'
            for child in node.children:
                yield from encode(child)
            yield '$'

        return ','.join(encode(root))

    def deserialize(self, data: str) -> 'Node':
        def decode(I) -> 'Node':
            item = next(I, None)
            if not item or item == '$': return None
            node = Node(item, [])
            while child := decode(I):
                node.children.append(child)
            return node

        return decode(iter(data.split(',')))


# https://leetcode.com/problems/find-duplicate-subtrees/
class Solution652:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dup = defaultdict(int)

        @lru_cache(None)
        def seralization(node):
            if not node: return '#'
            return f'{node.val},{seralization(node.left)},{seralization(node.right)}'

        res = []

        def dfs(node):
            if not node: return
            key = seralization(node)

            if dup[key] == 1:
                res.append(node)

            dup[key] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res
