# In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once
# (allowing for revisiting vertices). this is Postorder Traversal
# the task of the problem can be interpreted
# as that given a list of flights (i.e. edges in graph), we should find an order to use each flight once and only once.
#
# In the resulted path, before we visit the last airport (denoted as V), we can say that we have already used all the
# rest flights, i.e. if there is any flight starting from V, then we must have already taken that before.

from collections import *
from typing import *


# https://leetcode.com/problems/reconstruct-itinerary/
class Solution332:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list) # cannot use set as value since the relationship: key - value edge
        for departure, arrival in sorted(tickets):
            graph[departure].append(arrival)

        res = []

        def dfs(node):
            dests = graph[node]
            while dests:
                to = dests.pop(0)  # remove node, so edge
                dfs(to)

            res.append(node)

        dfs('JFK')
        return res[::-1]
