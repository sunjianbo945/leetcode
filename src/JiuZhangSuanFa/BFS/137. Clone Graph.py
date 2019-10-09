"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here

        if not node: return None

        val_node_pair = self.cloneNodes(node)

        res = val_node_pair[node.label]

        queue = [node]
        visited = set()
        visited.add(node.label)
        while queue:

            old_node = queue.pop(0)
            new_node = val_node_pair[old_node.label]

            for old_neighbor in old_node.neighbors:
                new_neighbor = val_node_pair[old_neighbor.label]
                new_node.neighbors.append(new_neighbor)
                if old_neighbor.label not in visited:
                    queue.append(old_neighbor)
                    visited.add(old_neighbor.label)

        return res


    def cloneNodes(self, root):
        res = {}

        queue = [root]
        res[root.label] = UndirectedGraphNode(root.label)

        visited = set()
        visited.add(root.label)
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor.label not in visited:
                    res[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                    visited.add(neighbor.label)

        return res


one = UndirectedGraphNode(1)
two = UndirectedGraphNode(2)
four = UndirectedGraphNode(4)

one.neighbors.append(two)
one.neighbors.append(four)

two.neighbors.append(one)
two.neighbors.append(four)

four.neighbors.append(one)
four.neighbors.append(two)

Solution().cloneGraph(one)