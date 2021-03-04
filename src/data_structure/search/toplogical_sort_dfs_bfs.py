#
# a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for
# every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
# Application : System build
#               apt-get
#               Task-scheduling
#               pre-request

# Kahn’s algorithm
#
# The Kahn’s algorithm takes the bfs approach:
#
#
#     Take an in-degree array which will keep track of
#     Traverse the array of edges and simply increase the counter of the destination node by 1.
#
#     for each node in Nodes
#         indegree[node] = 0;
#     for each edge(src, dest) in Edges
#         indegree[dest]++
#
#     Time Complexity: O(V+E)
#     Traverse the list for every node and then increment the in-degree of all the nodes connected to it by 1.
#
#         for each node in Nodes
#             If (list[node].size()!=0) then
#             for each dest in list
#                 indegree[dest]++;
#
#     Time Complexity: The outer for loop will be executed V number of times and the inner for loop will be executed
#     E number of times, Thus overall time complexity is O(V+E).
#
#     The overall time complexity of the algorithm is O(V+E)


from collections import deque, defaultdict, Counter
from typing import List


class Solution:
    VISITING = -1
    VISITED = 1

    def topological_sort_dfs(self, graph):
        orders = deque()
        seen = defaultdict(int)

        def dfs(v):
            if seen[v] == self.VISITING:
                return False  # cycle detected

            if seen[v] == self.VISITED:
                return True  # visited already

            seen[v] = self.VISITING
            if all(dfs(n) for n in graph.get(v, [])):
                seen[v] = self.VISITED
                orders.appendleft(v)
                return True

            return False

        for node in graph:
            if not dfs(node):
                raise Exception('cycle detected')

        return orders


# https://leetcode.com/problems/course-schedule/
class Solution207:
    VISITING = -1
    VISITED = 1

    def canFinish_dfs(self, N: int, prerequisites: List[List[int]]) -> bool:
        seen = defaultdict(int)  # use seen to remove edge
        graph = defaultdict(list)
        for course, prerequest in prerequisites:
            graph[prerequest].append(course)

        def dfs(v):
            if seen[v] == self.VISITING: return False  # cycle detected
            if seen[v] == self.VISITED: return True  # visited already

            seen[v] = self.VISITING
            if all(dfs(neighbor) for neighbor in graph[v]):
                seen[v] = self.VISITED
                return True

            return False

        for i in range(N):
            if not dfs(i):
                return False

        return True

    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        lock = defaultdict(int)

        for course, prerequest in prerequisites:
            graph[prerequest].append(course)
            lock[course] += 1

        queue = []
        taken = 0
        for i in range(numCourses):
            if not lock[i]:
                queue.append(i)

        while queue:
            taken += 1
            node = queue.pop(0)
            for neighbor in graph[node]:
                lock[neighbor] -= 1
                if not lock[neighbor]:
                    queue.append(neighbor)

        return True if taken == numCourses else False


# https://leetcode.com/problems/course-schedule-ii/
class Solution210:
    VISITING = -1
    VISITED = 1

    def findOrder_dfs(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        orders = []
        seen = defaultdict(int)  # use seen to remove edge
        graph = defaultdict(list)
        for course, prerequest in prerequisites:
            graph[prerequest].append(course)

        def dfs(v):
            if seen[v] == self.VISITING: return False  # cycle detected
            if seen[v] == self.VISITED: return True  # visited already

            seen[v] = self.VISITING
            if all(dfs(neighbor) for neighbor in graph[v]):
                seen[v] = self.VISITED
                orders.append(v)
                return True

            return False

        for i in range(N):
            if not dfs(i):
                return []

        return orders

    def findOrder_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        lock = defaultdict(int)

        for course, prerequest in prerequisites:
            graph[prerequest].append(course)
            lock[course] += 1

        queue = []
        seen = []
        for i in range(numCourses):
            if not lock[i]:
                queue.append(i)
                seen.append(i)

        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                lock[neighbor] -= 1
                if not lock[neighbor]:
                    seen.append(neighbor)
                    queue.append(neighbor)

        return seen if len(seen) == numCourses else []


# https://leetcode.com/problems/parallel-courses/
class Solution1136:
    def minimumSemesters_bfs(self, N: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        lock = defaultdict(int)
        for u, v in relations:
            graph[u].add(v)
            lock[v] += 1

        queue = [i for i in range(1, N + 1) if lock[i] == 0]
        taken = 0  # the number of course has been taken
        level = 0
        while queue:
            size = len(queue)
            taken += len(queue)
            for _ in range(size):
                node = queue.pop(0)

                for neighbor in graph[node]:
                    lock[neighbor] -= 1
                    if lock[neighbor] == 0:
                        queue.append(neighbor)

            level += 1

        return level if taken == N else -1

    VISITING = -1

    def minimumSemesters_dfs(self, N: int, relations: List[List[int]]) -> int:
        seen = defaultdict(int)  # use seen to remove edge
        graph = defaultdict(list)
        for course, prerequest in relations:
            graph[prerequest].append(course)

        # here can use @lru_cache(None)
        def dfs(v):
            if seen[v] == self.VISITING: return -1  # cycle detected
            if seen[v] > 0: return seen[v]  # visited already

            seen[v] = self.VISITING
            res = 0
            for neighbor in graph[v]:
                if (length := dfs(neighbor)) == -1: return -1
                res = max(res, length + 1)

            seen[v] = res
            return res

        res = 0
        for i in range(1, N + 1):
            length = dfs(i)
            if length == -1: return -1
            res = max(res, length + 1)

        return res


# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution953:  # this is not dfs or bfs question, but it is the derivative of the alien dictionary
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_index = defaultdict(int)  # 'h' -> 0
        for idx, char in enumerate(order):
            letter_index[char] = idx

        for w1, w2 in zip(words, words[1:]):
            for char1, char2 in zip(w1, w2):
                if char1 == char2: continue
                if letter_index[char1] > letter_index[char2]: return False
                break
            else:
                if len(w2) < len(w1): return False

        return True


# https://leetcode.com/problems/alien-dictionary/
class Solution426:
    def alienOrder_bfs(self, words: List[str]) -> str:
        # words: ["wrt","wrf","er","ett","rftt"]
        unlock = defaultdict(set)
        dpendency_count = Counter({c: 0 for word in words for c in word})
        # the following part builds the graph and the dependency count
        # zip(words, words[1:]) -> [('wrt', 'wrf'), ('wrf', 'er'), ('er', 'ett'), ('ett', 'rftt')]
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:  # Very important => [za, zb, ca, cb] => a->b edge should not be added twice to in_degree!
                    if d not in unlock[c]:
                        unlock[c].add(d)
                        dpendency_count[d] += 1
                    break  # find the first difference, then break, no need to compare the later items
            else:
                # Check that second word isn't a prefix of first word... ["abc","ab"] -> ""
                if len(second_word) < len(first_word): return ""
        # bfs
        output = []
        queue = [c for c in dpendency_count if dpendency_count[c] == 0]
        while queue:
            c = queue.pop(0)
            output.append(c)
            for d in unlock[c]:
                dpendency_count[d] -= 1
                if dpendency_count[d] == 0:
                    queue.append(d)

        if len(output) < len(dpendency_count):
            return ""

        return "".join(output)

    VISITING = -1
    VISITED = 1

    def alienOrder_dfs(self, words: List[str]) -> str:
        graph = {c: [] for word in words for c in word}  # some words does not have edge
        # zip(words, words[1:]) -> [('wrt', 'wrf'), ('wrf', 'er'), ('er', 'ett'), ('ett', 'rftt')]
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:  # Very important => [za, zb, ca, cb] => a->b edge should not be added twice to in_degree!
                    if d not in graph[c]:
                        graph[c].append(d)
                    break  # find the first difference, then brreak, no need to compare the later items
            else:
                # Check that second word isn't a prefix of first word... ["abc","ab"] -> ""
                if len(second_word) < len(first_word): return ""

        seen = defaultdict(int)
        res = []

        def dfs(v):
            if seen[v] == self.VISITING: return False
            if seen[v] == self.VISITED: return True

            seen[v] = self.VISITING

            if all(dfs(neighbor) for neighbor in graph[v]):
                seen[v] = self.VISITED
                res.append(v)
                return True

            return False

        if not all(dfs(v) for v in graph):
            return ''

        return "".join(res[::-1])


# https://leetcode.com/problems/minimum-height-trees/
class Solution310:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        lock = defaultdict(int)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

            lock[u] += 1
            lock[v] += 1

        queue = [node for node in range(n) if lock[node] <= 1]  # all leaves
        pre = []
        while queue:
            size = len(queue)
            pre = list(queue)
            for _ in range(size):
                node = queue.pop(0)
                for neighbor in graph[node]:
                    lock[neighbor] -= 1
                    if lock[neighbor] == 1:
                        queue.append(neighbor)

        return pre


# https://leetcode.com/problems/keys-and-rooms/
class Solution841:
    def canVisitAllRooms_bfs(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        m, n = len(rooms), len(rooms[0])
        for room in range(m):
            keys = rooms[room]
            graph[room].extend(keys)

        queue = [0]
        seen = {0}
        count = 0
        while queue:
            room = queue.pop(0)

            count += 1

            for nRoom in graph[room]:
                if nRoom in seen: continue

                seen.add(nRoom)
                queue.append(nRoom)

        return count == m

    def canVisitAllRooms_dfs(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        m, n = len(rooms), len(rooms[0])
        for room in range(m):
            keys = rooms[room]
            graph[room].extend(keys)

        seen = set()

        def dfs(room):
            if room in seen: return

            seen.add(room)
            for neighbor in graph[room]:
                dfs(neighbor)

        dfs(0)
        return len(seen) == m
