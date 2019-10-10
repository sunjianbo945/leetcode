#  [LintCode] 431 Connected Component in Undirected Graph 解题报告
# Description
# Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)
#
# Notice
# Each connected component should sort by label.
#
#
# Clarification
# Learn more about representation of graphs
#
#
# Example
# Given graph:
#
# A------B  C
#   \         |   |
#     \       |   |
#       \     |   |
#         \   |   |
#           D   E
# Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

# union find algorithm
# Disjoint-set/Union-find Forest
# Find(x): find the root/cluster-id of x
# Union(x,y), merge two clusters




class UndirectedGraphNode:
    def __init__(self, x):
        self.label=x
        self.neighbors = []



class Solution:
    '''
    :param nodes: list of UndirectedGraphNode

    '''
    def connectedSet(self, nodes):
        pass

