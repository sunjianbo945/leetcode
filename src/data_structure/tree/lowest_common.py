from collections import *

from src.data_structure.tree.model import TreeNode, Node


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class Solution235:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # O(n) since all nodes are in a line
        if not root: return None

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root

    def lowestCommonAncestor_iterative(self, root, p, q):
        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:
            # Value of current node or parent node.
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution236:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root.val == p.val or root.val == q.val: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: return root
        if left: return left
        return right


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
class Solution1644:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = defaultdict(int)  # O(n)

        def dfs(node):
            if not node: return

            if node.left:
                parents[node.left] = node
                dfs(node.left)

            if node.right:
                parents[node.right] = node
                dfs(node.right)

        dfs(root)  # O(n)

        if p not in parents or q not in parents: return None

        p_ancesoters = set()
        curr = p
        while curr:  # O(n)
            p_ancesoters.add(curr)
            curr = parents[curr]

        curr = q
        while curr:  # O(n)
            if curr in p_ancesoters:
                return curr

            curr = parents[curr]

        return None


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
class Solution1650:
    def lowestCommonAncestor(self, A: 'Node', B: 'Node') -> 'Node':
        A_map = {}
        temp = A
        while temp is not None:
            A_map[temp.val] = temp
            temp = temp.parent
        temp = B
        while temp is not None:
            if temp.val in A_map:
                return A_map[temp.val]
            temp = temp.parent

        return None


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
class Solution1676:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def dfs(node):
            if not node: return None
            if node in nodes: return node

            left, right = dfs(node.left), dfs(node.right)
            if left and right: return node

            return left or right

        return dfs(root)


# https://leetcode.com/problems/find-distance-in-a-binary-tree/
class Solution1740:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:

        def lca(node):
            if not node or node.val == p or node.val == q:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node
            else:
                return left or right

        def dist(node, target):
            if not node: return float('inf')
            if node.val == target:
                return 0

            return 1 + min(dist(node.left, target), dist(node.right, target))

        lca_node = lca(root)

        return dist(lca_node, p) + dist(lca_node, q)


# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
class Solution1123:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        nodes = set(self.findDeepestNode(root))
        print(nodes)

        def dfs(node):
            if not node: return
            if node in nodes: return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: return node
            return left or right

        return dfs(root)

    def findDeepestNode(self, root):
        queue = [root]
        pre = []
        while queue:  # O(n)
            size = len(queue)
            pre = []
            for _ in range(size):
                node = queue.pop(0)
                pre.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return pre

    def lcaDeepestLeaves_better(self, root):
        self.lca, self.deepest = None, 0

        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)

        helper(root, 0)
        return self.lca
