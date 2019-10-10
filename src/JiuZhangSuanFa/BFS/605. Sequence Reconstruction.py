class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here

        graph = self.create_graph(seqs)

        indegree = self.count(seqs)

        queue = []
        res = []
        for key, val in indegree.items():
            if val == 0:
                queue.append(key)
                res.append(key)

        while queue:

            if len(queue) > 1:
                return False

            cur = queue.pop(0)

            for neighbor in graph.get(cur, []):

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    res.append(neighbor)

        return res == org

    def count(self, seqs):
        res = {}

        for order in seqs:
            if not order:continue

            for i in range(len(order) - 1, 0, -1):
                if order[i] not in res:
                    res[order[i]] = {order[i - 1]}
                else:
                    res[order[i]].add(order[i - 1])

            if order[0] not in res:
                res[order[0]] = set()

        indegree = {}
        for key, val in res.items():
            indegree[key] = len(val)

        return indegree

    def create_graph(self, seqs):

        res = {}

        for order in seqs:
            if not order:continue

            for i in range(len(order) - 1, 0, -1):
                if order[i - 1] not in res:
                    res[order[i - 1]] = {order[i]}
                else:
                    res[order[i - 1]].add(order[i])

        return res