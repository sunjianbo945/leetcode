class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here

        graph = self.create_graph(prerequisites)
        indegree = self.count(prerequisites)
        queue = []
        visited = set()
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
                visited.add(i)

        while queue:

            node = queue.pop(0)

            for neighbor in graph.get(node, []):

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return len(visited) == numCourses

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
