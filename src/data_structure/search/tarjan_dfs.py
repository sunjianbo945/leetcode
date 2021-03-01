import math
from collections import *
from typing import *


# Tarjan's strongly connected components algorithm is an algorithm in graph theory for finding the
# strongly connected components (SCCs) of a directed graph.

# https://leetcode.com/problems/critical-connections-in-a-network/
class Solution1192:
    def criticalConnections_edges(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        minStep = {}
        res = []

        def dfs(node, pre, step):
            if node in minStep: return
            minStep[node] = step

            # label all steps
            for neighbor in graph[node]:
                if neighbor != pre:
                    dfs(neighbor, node, step + 1)

            for neighbor in graph[node]:
                if neighbor != pre:
                    minStep[node] = min(minStep[node], minStep[neighbor])

            if pre != -1 and minStep[node] > minStep[pre]:
                res.append([pre, node])

        dfs(0, -1, 0)
        return res


# Given an undirected graph, find out all the vertices when removed will make the graph disconnected. Initially the graph is connected.
#
# For example given the graph below:
#
#                1   7
#                |   |
#            2 - 3 - 6 - 0
#                |   |
#                4   5
#
# Return [3, 6]. Because we can make the graph disconnected by removing either vertex 3 or vertex 6.
#
# Input:
#
# nodeNum, the total count of vertices in the graph. Each vertex has an unique id in the range from 0 to nodeNum - 1 inclusive.
#
# edges, a list of integer pairs representing all the edges on the graph.
#
# output:
#
# A list of integers representing the ids of the articulation points.
#
# example:
#
# Input:
#
# nodeNum = 7
#
# edges = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]
#
# Output:
#
# [2,3,5]

class Solution:
    def patterns_articulation(self, edges):
        graph = defaultdict(set)
        for idx, edge in enumerate(edges):
            if not edge: continue
            for e in edge:
                graph[idx].add(e)
                graph[e].add(idx)

        min_step = {0: math.inf}  # this setting 0 used as pre
        articulation = set()

        def dfs(curr, pre, step):
            if curr in min_step: return
            min_step[curr] = step

            for neighbor in graph[curr]:
                if neighbor == pre: continue
                dfs(neighbor, curr, step + 1)

            for neighbor in graph[curr]:
                if neighbor == pre: continue
                min_step[curr] = min(min_step[curr], min_step[neighbor])

            if pre in min_step and min_step[curr] > min_step[pre] and len(graph[curr]) < 2:
                articulation.add(pre)

        for key, val in graph.items():
            if len(val) > 1 and key not in min_step:
                dfs(key, 0, 0)
        return articulation


print(Solution().patterns([[], [2], [1, 4, 5], [5], [2, 5], [2, 3, 4, 5], [5]]))
