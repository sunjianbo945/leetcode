from typing import List

# a structure to represent a graph
# template
class DisjointSet:
    def __init__(self, num_of_v):
        self.parent = [i for i in range(num_of_v)]
        self.rank = [0] * num_of_v

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if self.rank[u] > self.rank[v]:
            self.parent[pv] = pu
        elif self.rank[u] < self.rank[v]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[u] += 1


# https://leetcode.com/problems/graph-valid-tree/
class Solution216:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        g = DisjointSet(n)

        for u, v in edges:
            pu, pv = g.find(u), g.find(v)
            if pu == pv:
                return False
            else:
                g.union(u, v)

        return True
