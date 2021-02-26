# Amazon is trying to understand customer shopping patterns and offer items that are regularly bought together to new customers. Each item that has been bought together can be represented as an undirected graph where edges join often bundled products. A group of n products is uniquely numbered from 1 of product_nodes. A trio is defined as a group of three related products that all connected by an edge. Trios are scored by counting the number of related products outside of the trio, this is referred as a product sum.
#
# Given product relation data, determine the minimum product sum for all trios of related products in the group. If no such trio exists, return -1.
#
# Example
# products_nodes = 6
# products_edges = 6
# products_from = [1,2,2,3,4,5]
# products_to = [2,4,5,5,5,6]
# Product 	Related Products
# 1 	2
# 2 	1, 4, 5
# 3 	5
# 4 	2, 5
# 5 	2, 3, 4, 6
# 6 	5
#
# A graph of n = 6 products where the only trio of related products is (2, 4, 5).
#
# The product scores based on the graph above are:
# Product 	Outside Products 	Which Products Are Outside
# 2 	1 	1
# 4 	0
# 5 	2 	3, 6
#
# In the diagram above, the total product score is 1 + 0 + 2 = 3 for the trio (2, 4, 5).
#
# Function Description
#
# Complete the function getMinScore in the editor below.
#
# getMinScore has the following parameter(s):
#
#    int products_nodes: the total number of products
#
#    int products_edges the total number of edges representing related products
#
#    int products_from[products_nodes]: each element is a node of one side of an edge.
#
#    int products_to[products edges]: each products_to[i] is a node connected to products_from[i]
#
# Returns:
#
# int: the minimum product sum for all trios of related products in the group. If no such trio exists, return -1.
#
# Constraints
#
#     1 <= products_nodes <= 500
#     1 <= products_edges <= min(500, (products_nodes * (products_nodes - 1)) / 2)
#     1 <= products_from[i], products to[i] <= products_nodes
#     products_from[i] != products_to[i]

from collections import defaultdict


class Solution:
    def patterns(self, N, edges):
        graph = defaultdict(set)
        for idx, edge in enumerate(edges):
            if not edge: continue
            for e in edge:
                graph[idx].add(e)
                graph[e].add(idx)

        res = float('inf')
        for i in range(1, N + 1):
            if len(graph[i]) < 2: continue
            for j in graph[i]:
                if len(graph[j]) < 2 or j <= i: continue
                for k in graph[j]:
                    if k > j and i in graph[k]:
                        # trio
                        res = min(res, len(graph[i]) + len(graph[j]) + len(graph[k]) - 6)
                        # print(i, j, k, len(graph[i]), len(graph[j]), len(graph[k]), graph[k])
        return res


print(Solution().patterns(6, [[], [2], [1, 4, 5], [5], [2, 5], [2, 3, 4], [5]]))
print(Solution().patterns(5, [[], [2, 3], [3, 4], [4], [5]]))
