"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        res = []

        if not graph: return res

        # indegree
        indegree = self.count_degree(graph)

        #free element
        queue = []
        for node in graph:
            if node not in indegree:
                queue.append(node)
                res.append(node)

        # sorting
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    res.append(neighbor)
                    queue.append(neighbor)

        return res

    def count_degree(self, graph):

        res = {}

        for node in graph:

            for neighbor in node.neighbors:

                if neighbor not in res:
                    res[neighbor] = 1
                else:
                    res[neighbor] += 1

        return res


