from collections import defaultdict
from heapq import *
from math import inf
from typing import List


# Bellman Ford algorithm:
# https://algs4.cs.princeton.edu/44sp/
# https://algs4.cs.princeton.edu/44sp/BellmanFordSP.java.html
# https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture14.pdf
# https://en.wikipedia.org/wiki/Bellman–Ford_algorithm
# https://www.geeks for geeks.org/bellman-ford-algorithm-dp-23/(remove the 2 spaces among the links to make it valid)
#
# Dijkstra's algorithm:
# https://algs4.cs.princeton.edu/44sp/
# https://algs4.cs.princeton.edu/44sp/DijkstraSP.java.html
# https://en.wikipedia.org/wiki/Dijkstra's_algorithm
# https://www.geeks for geeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ (remove the 2 spaces among the links to make it valid)
#
# Similar problems:
#
# 407. Trapping Rain Water II
# 499. The Maze III
# 505. The Maze II
# 743. Network Delay Time
# 787. Cheapest Flights Within K Stops
# 1631. Path With Minimum Effort

# Dijkstra Algorithm
# function Dijkstra(Graph, source):
#       create vertex set Q
#
#       for each vertex v in Graph:
#           dist[v] <- INFINITY
#           prev[v] <- UNDEFINED
#           add v to Q
#
#       dist[source] <- 0
#
#       while Q is not empty:
#           u <- vertex in Q with min dist[u]
#           remove u from Q
#
#           for each neighbor v of u:
#               alt <- dist[u] + length(u,v)
#               if alt < dist[v]
#                   dist[v] <- alt
#                   prev[v] <- u
#
#      return dist[], prev[]

# https://www.programiz.com/dsa/bellman-ford-algorithm
# function bellmanFord(G, S)
#   for each vertex V in G
#     distance[V] <- infinite
#       previous[V] <- NULL
#   distance[S] <- 0
#
#   for each vertex V in G
#     for each edge (U,V) in G
#       tempDistance <- distance[U] + edge_weight(U, V)
#       if tempDistance < distance[V]
#         distance[V] <- tempDistance
#         previous[V] <- U
#
#   for each edge (U,V) in G
#     If distance[U] + edge_weight(U, V) < distance[V}
#       Error: Negative Cycle Exists
#
#   return distance[], previous[]


# https://leetcode.com/problems/network-delay-time/
class Solution743:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, cost in times:
            graph[u].append((v, cost))

        heap = [(0, k)]
        seen = {}
        res = 0
        while heap:  # Dijkstra need to heap here O(ElogV)
            dis, node = heappop(heap)

            if node in seen: continue
            seen[node] = dis  # Dijkstra need to put seen here
            res = max(dis, res)

            for neighbor, cost in graph[node]:
                if neighbor in seen: continue

                heappush(heap, (dis + cost, neighbor))

        return res if len(seen) == n else -1


# https://leetcode.com/problems/path-with-maximum-minimum-value/
class Solution1102:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = [(-A[0][0], 0, 0)]
        seen = set()
        res = inf
        while heap:
            num, x, y = heappop(heap)

            if (x, y) in seen: continue
            seen.add((x, y))
            res = min(res, -num)

            if x == m - 1 and y == n - 1: return res

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen: continue
                heappush(heap, (-A[nx][ny], nx, ny))

        return -1


# https://leetcode.com/problems/path-with-maximum-probability/
class Solution1514:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        heap = [(-1, start)]
        seen = set()
        while heap:
            prob, node = heappop(heap)

            if node == end: return -prob
            if node in seen: continue
            seen.add(node)

            for neighbor, p in graph[node]:
                if neighbor in seen: continue

                heappush(heap, (p * prob, neighbor))

        return 0

# Bellman-Ford algorithm is a single-source shortest path algorithm, so when you have negative edge weight then it can
# detect negative cycles in a graph.
#
# The only difference between the two is that Bellman-Ford is also capable of handling negative weights whereas
# Dijkstra Algorithm can only handle positives.
#
# From wiki
#
#     However, Dijkstra's algorithm greedily selects the minimum-weight node that has not yet been processed,
#     and performs this relaxation process on all of its outgoing edges; in contrast, the Bellman–Ford algorithm
#     simply relaxes all the edges, and does this |V | − 1 times, where |V | is the number of vertices in the graph.
#     In each of these repetitions, the number of vertices with correctly calculated distances grows,
#     from which it follows that eventually all vertices will have their correct distances.
#     This method allows the Bellman–Ford algorithm to be applied to a wider class of inputs than Dijkstra.
#
# Dijkstra is however generally considered better in the absence of negative weight edges,
# as a typical binary heap priority queue implementation has O((|E|+|V|)log|V|) time complexity
# [A Fibonacci heap priority queue gives O(|V|log|V| + |E|)], while the Bellman-Ford algorithm has O(|V||E|) complexity
