from typing import List


# a structure to represent a graph
# template
class DisjointSet:
    def __init__(self, N):
        self.parents = list(range(N + 1))
        self.rank = [0] * (N + 1)

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if self.rank[pu] < self.rank[pv]:
            self.parents[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.rank[pu] += 1


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


# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
class Solution1135:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(N)
        total = 0
        cost = 0
        connections.sort(key=lambda x: x[2])
        for a, b, c in connections:
            if ds.find(a) == ds.find(b): continue
            ds.union(a, b)
            cost += c
            total += 1

        return cost if total == N - 1 else -1
