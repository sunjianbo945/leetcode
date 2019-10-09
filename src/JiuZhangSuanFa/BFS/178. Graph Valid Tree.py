class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    # # n nodes must has n-1 edges, and n nodes must be added
    def validTree(self, n, edges):
        # write your code here
        # no node then return False
        if n == 0: return False

        # n nodes must has n-1 edges
        if n - 1 != len(edges):
            return False
        # make graph
        graph = self.make_graph(edges)

        queue = [0]
        visited = {0}

        # bfs
        while queue:
            node = queue.pop(0)
            for neighbor in graph.get(node, []):
                if neighbor in visited:
                    continue

                queue.append(neighbor)
                visited.add(neighbor)

        return len(visited) == n

    def make_graph(self, edges):

        res = {}

        for edge in edges:

            if edge[0] not in res:
                res[edge[0]] = {edge[1]}
            else:
                res[edge[0]].add(edge[1])

            if edge[1] not in res:
                res[edge[1]] = {edge[0]}
            else:
                res[edge[1]].add(edge[0])

        return res
