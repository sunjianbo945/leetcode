from collections import *
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


# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
class Solution742:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = defaultdict(set)
        graph[root.val].add(float('inf'))  # add a dummy to let alog know it is root

        def dfs(node):
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                dfs(node.left)

            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                dfs(node.right)

        graph.setdefault(root.val, set())  # set default otherwise leaf will lose
        dfs(root)
        queue = list(node for node in graph if node and node == k)
        seen = set(queue)

        while queue:
            node = queue.pop(0)
            if len(graph[node]) <= 1 and node < float('inf'):  # only from parent
                return node

            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
class Solution863:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(set)

        def dfs(node):
            if not node: return

            if node.left:
                graph[node].add(node.left)
                graph[node.left].add(node)
                dfs(node.left)

            if node.right:
                graph[node].add(node.right)
                graph[node.right].add(node)
                dfs(node.right)

        graph.setdefault(root, set())
        dfs(root)

        queue = [target]
        seen = {target}
        while queue:
            size = len(queue)
            if K == 0: return [x.val for x in queue]
            for _ in range(size):
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

            K -= 1

        return []
