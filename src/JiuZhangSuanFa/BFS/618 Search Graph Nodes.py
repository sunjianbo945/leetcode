# Description
# Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.
#
# There is a mapping store the nodes' values in the given parameters.
#
# Notice
# It's guaranteed there is only one available solution
#
#
# Example
# 2------3 - 5
#  \        |     |
#    \      |     |
#      \    |     |
#        \  |     |
#          1 -- 4
# Give a node 1, target is 50
#
# there a hash named values which is [3,4,10,50,50], represent:
# Value of node 1 is 3
# Value of node 2 is 4
# Value of node 3 is 10
# Value of node 4 is 50
# Value of node 5 is 50
#
# Return node 4

class UndirectedGraphNode:
    def __init__(self,x):
        self.label = x
        self.neighbors = []


class Solution:

    def searchGraph(self, graph, values, node, target):

        if not node:return None

        queue = [node]

        visited = set()
        visited.add(node.label)

        while queue:

            cur = queue.pop(0)

            for neighbor in cur.neighbors:

                if neighbor.label in values and values[neighbor.label] == target:
                    return neighbor

                if neighbor.label not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor.label)

        return None







