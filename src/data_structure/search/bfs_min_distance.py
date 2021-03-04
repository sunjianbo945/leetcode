import math
from collections import defaultdict
from typing import *


# https://leetcode.com/problems/rotting-oranges/
class Solution994:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the minimum distance from 2 to all 1
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        queue = []
        seen = set()
        count_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:
                    count_fresh += 1
                else:
                    queue.append((i, j))

        if count_fresh == 0: return 0

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] != 1: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

            level += 1

        return level - 1 if len(seen) == count_fresh else -1


# https://leetcode.com/problems/as-far-from-land-as-possible/
class Solution1162:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        queue = []
        seen = set()
        for i in range(m):  # O(m*n)
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    seen.add((i, j))

        if not queue or len(queue) == m * n: return -1  # no land or no water

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] == 1: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

            level += 1  # the max dis is the level - 1

        return level - 1


# https://leetcode.com/problems/walls-and-gates/
class Solution286:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:  # O (m*n)
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find starting point
        queue = []
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(rooms), len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:  # gate
                    seen.add((i, j))
                    queue.append((i, j))

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)

                rooms[x][y] = level  # logic

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or rooms[nx][ny] == -1: continue

                    queue.append((nx, ny))
                    seen.add((nx, ny))

            level += 1


# https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution1091:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        directions = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                directions.append([i, j])

        queue = [(0, 0)]
        seen = {(0, 0)}
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)

                if x == m - 1 and y == n - 1:  # logic find the last then return
                    return level + 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] == 1: continue
                    seen.add((nx, ny))
                    queue.append((nx, ny))

            level += 1

        return -1


# https://leetcode.com/problems/best-meeting-point/
class Solution296:
    def minTotalDistance_bfs(self, grid: List[List[int]]) -> int:  # use bfs is TLE since O(m^2n^2) but nice to practise
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dis = [[0] * n for _ in range(m)]

        def bfs(x, y):
            queue = [(x, y)]
            level = 0
            seen = {(x, y)}
            while queue:
                size = len(queue)
                for _ in range(size):
                    x, y = queue.pop(0)

                    dis[x][y] += level

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen:
                            continue

                        seen.add((nx, ny))
                        queue.append((nx, ny))

            level += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                bfs(i, j)

        res = math.inf
        for i in range(m):
            for j in range(n):
                res = min(res, dis[i][j])

        return res


def minTotalDistance_math(self, grid):  # O(mn) sort + greedy
    m, n = len(grid), len(grid) and len(grid[0])
    # rows and cols are the person location sorted in order
    rows, cols = [i for i in range(m) for j in range(n) if grid[i][j]], [j for j in range(n) for i in range(m) if
                                                                         grid[i][j]]

    def min1d(points):
        l, r, dis = 0, len(points) - 1, 0
        while l < r:
            dis += points[r] - points[l]  # total distance l and r need to walk to meet
            l += 1
            r -= 1

        return dis

    return min1d(rows) + min1d(cols)


# https://leetcode.com/problems/shortest-distance-from-all-buildings/
class Solution317:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dis = [[0] * n for i in range(m)]
        seen = defaultdict(int)  # the i, j has been visited k times

        def bfs(x, y):  # x,y is building
            nonlocal num_house
            level = 0
            queue = [(x, y)]

            while queue:
                size = len(queue)
                for _ in range(size):
                    x, y = queue.pop(0)

                    dis[x][y] += level

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or seen[nx, ny] != num_house or grid[nx][ny] != 0:
                            continue

                        seen[nx, ny] += 1
                        queue.append((nx, ny))

                level += 1

        num_house = 0  # need to record how many houses
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    num_house += 1

        res = math.inf
        for i in range(m):
            for j in range(n):
                if seen[i, j] == num_house:
                    res = min(res, dis[i][j])

        return res if res < math.inf else -1


# https://leetcode.com/problems/jump-game-iv/
class Solution1345:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        for idx, num in enumerate(arr):
            graph[num].append(idx)

        n = len(arr)
        queue = [0]  # index queue
        seen = {0}

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                idx = queue.pop(0)

                if idx == n - 1:
                    return step

                for neighbor in [idx - 1, idx + 1, *graph[arr[idx]]]:
                    if neighbor < 0 or neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)

                graph[arr[idx]].clear()

            step += 1

        return -1


# https://leetcode.com/problems/bus-routes/
class Solution815:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # note routes length is small so we need to use routes to find the min dsitance
        if source == target: return 0
        # make graphs
        bus_routes = defaultdict(set)
        for route, buses in enumerate(routes):
            for bus in buses:
                bus_routes[bus].add(route)

        route_route = defaultdict(set)
        for route, buses in enumerate(routes):
            for bus in buses:
                route_route[route].update(bus_routes[bus])

        queue = [*bus_routes[source]]  # route
        target = bus_routes[target]  # target routes that can get on target bus
        seen = set(queue)

        stop = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                route = queue.pop(0)

                if route in target: return stop

                for neighbor in route_route[route]:
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)

            stop += 1

        return -1


# https://leetcode.com/problems/k-similar-strings/
class Solution854:
    def kSimilarity(self, A: str, B: str) -> int:
        #  the min distance K for which A and B are K-similar.
        queue = [A]
        K = 0
        seen = set()
        n = len(A)

        def get_neighbor(C):
            first_diff = 0
            for i in range(n):
                if C[i] != B[i]:
                    first_diff = i
                    break

            res = []
            for j in range(first_diff + 1, n):
                if C[j] == B[first_diff]:
                    res.append(C[:first_diff] + C[j] + C[first_diff + 1:j] + C[first_diff] + C[j + 1:])
            return res

        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.pop(0)
                if curr == B: return K

                for neighbor in get_neighbor(curr):
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)

            K += 1


# https://leetcode.com/problems/01-matrix/
class Solution542:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        # min distance from 0 to 1 cell
        m, n = len(A), len(A[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = [[0] * n for _ in range(m)]

        queue = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                res[x][y] = level
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

            level += 1

        return res


# https://leetcode.com/problems/shortest-path-to-get-food/
class Solution1730:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        seen = set()
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    seen.add((i, j))

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                if grid[x][y] == '#': return step

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] == 'X': continue
                    seen.add((nx, ny))
                    queue.append((nx, ny))

            step += 1

        return -1


# https://leetcode.com/problems/evaluate-division/
class Solution399:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (x, y), value in zip(equations, values):
            graph[x].append([y, value])
            graph[y].append([x, 1 / value])

        def bfs(start, target):
            queue = [(start, 1)]
            seen = {start}

            while queue:
                char, value = queue.pop(0)
                if char == target: return value

                for nchar, nvalue in graph[char]:
                    if nchar in seen: continue

                    seen.add(nchar)
                    queue.append([nchar, value * nvalue])

            return -1.0

        res = []
        for numerator, denominator in queries:
            if not graph[numerator] or not graph[denominator]:
                res.append(-1.0)
            elif numerator == denominator:
                res.append(1.0)
            else:
                res.append(bfs(numerator, denominator))

        return res