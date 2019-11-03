from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = self.create_graph(prerequisites)
        indegree = self.count(prerequisites)
        queue = []
        res = []
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
                res.append(i)

        while queue:

            node = queue.pop(0)

            for neighbor in graph.get(node, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    res.append(neighbor)

        return res if len(res) == numCourses else []

    def create_graph(self, prerequisites):

        res = {}

        for pair in prerequisites:

            if pair[1] not in res:
                res[pair[1]] = [pair[0]]
            else:
                res[pair[1]].append(pair[0])

        return res

    def count(self, prerequisites):

        res = {}

        for pair in prerequisites:

            if pair[0] not in res:
                res[pair[0]] = 1
            else:
                res[pair[0]] += 1

        return res

