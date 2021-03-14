from collections import *
from typing import *

from src.data_structure.tree.model import TreeNode, Node


# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution102:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        queue = [root]
        while queue:
            size = len(queue)
            nodes = []
            for _ in range(size):
                node = queue.pop(0)
                nodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(nodes)

        return res


# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
class Solution107:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        queue = [root]
        while queue:
            size = len(queue)
            nodes = []
            for _ in range(size):
                node = queue.pop(0)
                nodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(nodes)

        return res[::-1]


# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
class Solution429:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root: return res

        queue = [root]
        while queue:
            size = len(queue)
            nodes = []
            for _ in range(size):
                node = queue.pop(0)

                nodes.append(node.val)

                for child in node.children:
                    if child: queue.append(child)

            res.append(nodes)

        return res


# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
class Solution103:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        forward = True
        queue = [root]
        while queue:
            size = len(queue)
            nodes = []
            for _ in range(size):
                node = queue.pop(0)

                nodes.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if forward:
                res.append(nodes)
            else:
                res.append(nodes[::-1])
            forward = not forward
        return res


# https://leetcode.com/problems/cousins-in-binary-tree/
class Solution993:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root, None)]  # node, parent
        firstP = None  # the parent of either x or y
        while queue:
            size = len(queue)
            for _ in range(size):
                node, parent = queue.pop(0)

                if x == node.val or y == node.val:
                    if not firstP:
                        firstP = parent
                    else:
                        return not firstP == parent

                if node.left: queue.append((node.left, node))
                if node.right: queue.append((node.right, node))

            if firstP: return False

        return False


# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
class Solution314:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        columnTable = defaultdict(list)  # column => list
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            columnTable[column].append(node.val)

            if node.left: queue.append((node.left, column - 1))
            if node.right: queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]


# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
class Solution987:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)  # column as key, value is (row, node_value)
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, column = queue.popleft()
            columnTable[column].append([row, node.val])
            if node.left: queue.append((node.left, row + 1, column - 1))
            if node.right: queue.append((node.right, row + 1, column + 1))

        res = []
        for x in sorted(columnTable.keys()):  # sorted by column
            temp = []
            for row, val in sorted(columnTable[x]):  # sorted by row, then number
                temp.append(val)
            res.append(temp)

        return res


# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
class Solution117:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        def link(list_nodes):
            n = len(list_nodes)
            for i in range(n - 1):
                list_nodes[i].next = list_nodes[i + 1]

        queue = [root]
        while queue:
            size = len(queue)
            link(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return root


# https://leetcode.com/problems/binary-tree-right-side-view/
class Solution199:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []

        queue = [root]
        res = []
        while queue:
            size = len(queue)
            res.append(queue[-1].val)
            for _ in range(size):
                node = queue.pop(0)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res


# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
class Solution515:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            max_num = float('-inf')
            for _ in range(size):
                node = queue.pop(0)
                max_num = max(max_num, node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(max_num)

        return res


# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
class Solution1161:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        level = 1
        res = 1
        queue = [root]

        while queue:
            size = len(queue)
            s = 0
            for _ in range(size):
                node = queue.pop(0)
                s += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if s > max_sum:
                max_sum = s
                res = level
            level += 1

        return res


# https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution637:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        res = []
        queue = [root]

        while queue:
            size = len(queue)
            s, count = 0, 0
            for _ in range(size):
                node = queue.pop(0)
                s += node.val
                count += 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(s / count)

        return res
